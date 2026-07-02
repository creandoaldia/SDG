/**
 * SDG Localidades — Frontend JavaScript v3
 * Features: mascota interactiva, melodia finalizacion, fases animadas,
 * validacion 4 niveles, SSE pipeline.
 */

// ======================================================================
// ESTADO GLOBAL
// ======================================================================
const state = {
    files: [],
    isProcessing: false,
    isComplete: false,
    currentPhase: 'idle',
    progress: 0,
    completedPhaseKeys: [],
    phases: {
        'idle': { label: 'Inactivo', icon: '○', order: 0 },
        'ingestion': { label: 'Lectura de archivos', icon: '📂', order: 1 },
        'normalization': { label: 'Normalizacion de datos', icon: '🔧', order: 2 },
        'deduplication': { label: 'Deteccion de duplicados', icon: '🔍', order: 3 },
        'pivot_generation': { label: 'Tablas dinamicas Q1-Q6', icon: '📊', order: 4 },
        'indicator_calculation': { label: 'Calculo de indicadores', icon: '📈', order: 5 },
        'resumen_cifras': { label: 'Resumen de cifras', icon: '📋', order: 6 },
        'excel_generation': { label: 'Generacion de Excel', icon: '📁', order: 7 },
        'validation': { label: 'Validacion a 4 niveles', icon: '✅', order: 8 },
        'validation_l1': { label: 'Nivel 1: Validacion de entrada', icon: '1', order: 81 },
        'validation_l2': { label: 'Nivel 2: Validacion transformacion', icon: '2', order: 82 },
        'validation_l3': { label: 'Nivel 3: Validacion contra original', icon: '3', order: 83 },
        'validation_l4': { label: 'Nivel 4: Validacion de salida', icon: '4', order: 84 },
        'completed': { label: '¡Completado!', icon: '🎉', order: 9 },
        'error': { label: 'Error', icon: '❌', order: 99 },
    },
    eventSource: null,
    mascotRotationIndex: 0,
    _rotationTimer: null,
    isSleeping: false,
    _sleepTimer: null,
    _bouncedIn: false
};

// Mascota rotacion: 3 estados que rotan durante procesamiento
const MASCOT_ROTATION_CYCLE = ['reading', 'analyzing', 'watching'];
const MASCOT_ROTATION_THOUGHTS = {
    reading: 'Leyendo archivos...',
    analyzing: 'Analizando datos...',
    watching: 'Observando indicadores...'
};
const MASCOT_ROTATION_INTERVAL_MS = 4000; // 4 segundos por estado

// Mascota pensamientos por fase
const MASCOT_THOUGHTS = {
    idle: '',
    reading: 'Leyendo archivos... 📖',
    analyzing: 'Analizando datos... 🔍',
    watching: 'Observando indicadores...',
    repairing: '¡A reparar! 🔧',
    driving: '¡A toda velocidad! 🚗',
    dancing: '¡Mision cumplida! 🎉',
    error: '¡Oh no! Algo salio mal...'
};

// Mascota estados SVG por fase
const MASCOT_STATES = {
    idle: 'idle',
    ingestion: 'reading',
    normalization: 'reading',
    deduplication: 'repairing',
    pivot_generation: 'analyzing',
    indicator_calculation: 'watching',
    resumen_cifras: 'analyzing',
    excel_generation: 'reading',
    validation: 'repairing',
    validation_l1: 'repairing',
    validation_l2: 'repairing',
    validation_l3: 'repairing',
    validation_l4: 'repairing',
    completed: 'dancing',
    error: 'idle'
};

// ======================================================================
// REFERENCIAS DOM
// ======================================================================
const dom = {
    dropZone: document.getElementById('dropZone'),
    fileInput: document.getElementById('fileInput'),
    selectFilesBtn: document.getElementById('selectFilesBtn'),
    filesPreview: document.getElementById('filesPreview'),
    fileList: document.getElementById('fileList'),
    fileCount: document.getElementById('fileCount'),
    clearFilesBtn: document.getElementById('clearFilesBtn'),
    uploadIcon: document.getElementById('uploadIcon'),
    processBtn: document.getElementById('processBtn'),
    processBtnText: document.getElementById('processBtnText'),
    processIcon: document.getElementById('processIcon'),
    mascotContainer: document.getElementById('mascotContainer'),
    mascotThought: document.getElementById('mascot-thought'),
    mascotThoughtText: document.getElementById('mascot-thought-text'),
    pipelineContainer: document.getElementById('pipelineContainer'),
    pipelineTitle: document.getElementById('pipelineTitle'),
    pipelineStatusDot: document.getElementById('pipelineStatusDot'),
    progressBar: document.getElementById('progressBar'),
    progressLabel: document.getElementById('progressLabel'),
    progressPercent: document.getElementById('progressPercent'),
    phasesTimeline: document.getElementById('phasesTimeline'),
    completedPhases: document.getElementById('completedPhases'),
    pendingPhases: document.getElementById('pendingPhases'),
    detailLog: document.getElementById('detailLog'),
    resultContainer: document.getElementById('resultContainer'),
    resultMessage: document.getElementById('resultMessage'),
    resultDetails: document.getElementById('resultDetails'),
    downloadBtn: document.getElementById('downloadBtn'),
    newProcessBtn: document.getElementById('newProcessBtn'),
    selectMonth: document.getElementById('selectMonth'),
    selectYear: document.getElementById('selectYear'),
    quickProcessBtn: document.getElementById('quickProcessBtn'),
    uploadIcon: document.getElementById('uploadIcon'),
};

// ======================================================================
// MASCOTA
// ======================================================================

// ─── Eye Tracking: pupilas siguen el cursor ───
let _eyeTrackingActive = false;
function setupEyeTracking() {
    const svg = document.getElementById('mascotSvg');
    if (!svg) return;
    const pupils = [
        { el: null, cx: 41, cy: 45, baseX: 41, baseY: 45, maxD: 1.8 },
        { el: null, cx: 71, cy: 45, baseX: 71, baseY: 45, maxD: 1.8 }
    ];
    // Get the pupil AND iris elements
    const allPupils = svg.querySelectorAll('circle[fill="#1a1a2e"]');
    const allIrises = svg.querySelectorAll('ellipse[fill="url(#pk-eye-iris)"]');
    if (allPupils.length >= 4 && allIrises.length >= 4) {
        pupils[0].pupil = allPupils[0];   // left eye pupil
        pupils[1].pupil = allPupils[1];   // right eye pupil
        pupils[0].iris = allIrises[0];    // left eye iris
        pupils[1].iris = allIrises[1];    // right eye iris
        pupils[0].shine = allPupils[2];   // left eye shine (3rd circle)
        pupils[1].shine = allPupils[3];   // right eye shine (4th circle)
    } else {
        return;
    }
    const container = dom.mascotContainer;
    if (!container) return;
    document.addEventListener('mousemove', (e) => {
        if (state.isSleeping || state.isProcessing) return;
        const rect = container.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const dx = (e.clientX - cx) / (rect.width / 2);
        const dy = (e.clientY - cy) / (rect.height / 2);
        const dist = Math.sqrt(dx*dx + dy*dy);
        const clamp = Math.min(dist, 1);
        const nx = dx / (dist || 1) * clamp;
        const ny = dy / (dist || 1) * clamp;
        pupils.forEach(p => {
            if (p.pupil && p.iris) {
                const px = p.baseX + nx * p.maxD;
                const py = p.baseY + ny * p.maxD;
                // Move pupil (circle)
                p.pupil.setAttribute('cx', px);
                p.pupil.setAttribute('cy', py);
                // Move iris (ellipse) together with pupil
                p.iris.setAttribute('cx', px);
                p.iris.setAttribute('cy', py);
                // Move eye shine too
                if (p.shine) {
                    p.shine.setAttribute('cx', px + 2);
                    p.shine.setAttribute('cy', py - 4);
                }
            }
        });
    });
}

// ─── Reset pupil + iris positions ───
function resetPupils() {
    const svg = document.getElementById('mascotSvg');
    if (!svg) return;
    const pupils = svg.querySelectorAll('circle[fill="#1a1a2e"]');
    const irises = svg.querySelectorAll('ellipse[fill="url(#pk-eye-iris)"]');
    if (pupils.length >= 4 && irises.length >= 4) {
        [41, 71].forEach((cx, i) => {
            pupils[i].setAttribute('cx', cx);
            pupils[i].setAttribute('cy', '45');
            irises[i].setAttribute('cx', cx);
            irises[i].setAttribute('cy', '45');
            if (i < 2) {
                pupils[i+2].setAttribute('cx', cx + 2);
                pupils[i+2].setAttribute('cy', '41');
            }
        });
        // Also reset the shine circles
        if (pupils.length >= 6) {
            pupils[4].setAttribute('cx', '39');
            pupils[4].setAttribute('cy', '49');
            pupils[5].setAttribute('cx', '69');
            pupils[5].setAttribute('cy', '49');
        }
    }
}

// ─── Inactividad -> Sueno ───
const SLEEP_TIMEOUT_MS = 5000;
function resetSleepTimer() {
    if (state._sleepTimer) {
        clearTimeout(state._sleepTimer);
        state._sleepTimer = null;
    }
    if (state.isProcessing || state.isComplete) return;
    state._sleepTimer = setTimeout(() => goToSleep(), SLEEP_TIMEOUT_MS);
}
function cancelSleepTimer() {
    if (state._sleepTimer) {
        clearTimeout(state._sleepTimer);
        state._sleepTimer = null;
    }
}
function goToSleep() {
    if (state.isProcessing || state.isSleeping) return;
    state.isSleeping = true;
    stopMascotRotation();
    setMascotState('sleeping');
    showMascotThought('Zzz... contando ovejas...');
    resetPupils();
}
function wakeUp() {
    if (!state.isSleeping) return;
    state.isSleeping = false;
    cancelSleepTimer();
    // Bounce animacion al despertar
    const container = dom.mascotContainer;
    container.classList.remove('mascot-bounce-in');
    container.classList.add('mascot-bounce-wake');
    setMascotState('idle');
    showMascotThought('¡Desperté! ¿Procesamos?');
    setTimeout(() => {
        container.classList.remove('mascot-bounce-wake');
        showMascotThought('');
        resetSleepTimer();
    }, 1500);
}

// ─── Actividad del usuario -> reset sleep timer ───
function setupActivityListeners() {
    const events = ['mousemove', 'click', 'keydown', 'scroll', 'touchstart'];
    const handler = () => {
        if (state._bouncedIn && !state.isProcessing && !state.isSleeping) {
            resetSleepTimer();
        }
    };
    events.forEach(ev => document.addEventListener(ev, handler, { passive: true }));
}

// ─── Interaccion: mascota trepa archivos y reacciona a hover ───
function setupMascotInteraction() {
    const container = dom.mascotContainer;
    if (!container) return;

    // Trepar cuando hay archivos cargados
    dom.dropZone.addEventListener('mouseenter', () => {
        if (state.files.length > 0 && !state.isProcessing) {
            container.style.transition = 'transform 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)';
            container.style.transform = 'translateY(-8px) scale(1.08)';
        }
    });
    dom.dropZone.addEventListener('mouseleave', () => {
        container.style.transform = '';
    });

    // Reaccionar al boton procesar
    dom.processBtn.addEventListener('mouseenter', () => {
        if (!state.isProcessing && state.files.length > 0) {
            container.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
            container.style.transform = 'translateX(6px) scale(1.1) rotate(3deg)';
        }
    });
    dom.processBtn.addEventListener('mouseleave', () => {
        container.style.transform = '';
    });

    // Trepar sobre archivos individuales (efecto al hacer clic en select)
    dom.selectFilesBtn.addEventListener('mouseenter', () => {
        if (!state.isProcessing) {
            container.style.transition = 'transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1)';
            container.style.transform = 'translateY(-12px) scale(1.05)';
        }
    });
    dom.selectFilesBtn.addEventListener('mouseleave', () => {
        container.style.transform = '';
    });
}

function setMascotState(stateName) {
    const container = dom.mascotContainer;
    if (!container) return;

    // Remover TODOS los estados anteriores
    const stateClasses = [
        'mascot-idle', 'mascot-reading', 'mascot-analyzing',
        'mascot-watching', 'mascot-repairing', 'mascot-driving',
        'mascot-dancing', 'mascot-sleeping', 'mascot-thought-visible'
    ];
    container.classList.remove(...stateClasses);

    // Agregar nuevo estado
    if (stateName) {
        container.classList.add(`mascot-${stateName}`);
    } else {
        container.classList.add('mascot-idle');
    }
}

// Inicia rotacion de 3 estados durante procesamiento
function startMascotRotation() {
    stopMascotRotation();
    state.mascotRotationIndex = 0;
    const firstState = MASCOT_ROTATION_CYCLE[0];
    setMascotState(firstState);
    showMascotThought(MASCOT_ROTATION_THOUGHTS[firstState]);
    state._rotationTimer = setInterval(() => {
        state.mascotRotationIndex = (state.mascotRotationIndex + 1) % MASCOT_ROTATION_CYCLE.length;
        const rotState = MASCOT_ROTATION_CYCLE[state.mascotRotationIndex];
        setMascotState(rotState);
        showMascotThought(MASCOT_ROTATION_THOUGHTS[rotState]);
    }, MASCOT_ROTATION_INTERVAL_MS);
}

function stopMascotRotation() {
    if (state._rotationTimer) {
        clearInterval(state._rotationTimer);
        state._rotationTimer = null;
    }
}

function showMascotThought(text) {
    const thought = dom.mascotThought;
    const textEl = dom.mascotThoughtText;
    if (!thought || !textEl) return;
    if (text) {
        textEl.textContent = text;
        thought.classList.add('opacity-100');
        thought.classList.remove('opacity-0');
    } else {
        thought.classList.remove('opacity-100');
        thought.classList.add('opacity-0');
    }
}

// ======================================================================
// MELODIA DE FINALIZACION (estilo lavadora)
// ======================================================================

function playCompletionMelody() {
    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();

        // Notas: DO-RE-MI-FA ascendente alegre
        const notes = [
            { freq: 523.25, time: 0 },     // DO5
            { freq: 587.33, time: 0.15 },   // RE5
            { freq: 659.25, time: 0.3 },    // MI5
            { freq: 783.99, time: 0.45 },   // SOL5 (mas agudo)
            { freq: 1046.5, time: 0.7 },    // DO6
            { freq: 783.99, time: 0.85 },   // SOL5
            { freq: 1046.5, time: 1.0 },    // DO6 (final)
        ];

        notes.forEach(({ freq, time }) => {
            const osc = ctx.createOscillator();
            const gain = ctx.createGain();
            osc.type = 'sine';
            osc.frequency.value = freq;
            gain.gain.setValueAtTime(0.3, time);
            gain.gain.exponentialRampToValueAtTime(0.01, time + 0.4);
            osc.connect(gain);
            gain.connect(ctx.destination);
            osc.start(time);
            osc.stop(time + 0.4);
        });
    } catch(e) { /* fallback */ }
}

// ======================================================================
// ARCHIVOS REQUERIDOS
// ======================================================================
const REQUIRED_PATTERNS = [
    { key: 'pqrs', label: 'BD PQRS Bogota Te Escucha', pattern: /bogota.*escucha|pqrs/i },
    { key: 'sac', label: 'SAC Atencion al Ciudadano', pattern: /sac_atencion/i },
    { key: 'side', label: 'Resumen SIDE', pattern: /resumen.*side/i },
    { key: 'cr', label: 'Productividad CR', pattern: /productividad.*cr/i },
    { key: 'ph', label: 'Productividad PH', pattern: /productividad.*ph/i },
    { key: 'encuestas', label: 'Reporte Encuestas', pattern: /productividad.*encuesta|encuesta.*productividad/i },
];

// ======================================================================
// DRAG & DROP
// ======================================================================
function setupDragDrop() {
    const dz = dom.dropZone;
    dom.selectFilesBtn.addEventListener('click', (e) => { e.stopPropagation(); dom.fileInput.click(); });
    dz.addEventListener('click', () => dom.fileInput.click());
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(ev => {
        dz.addEventListener(ev, (e) => { e.preventDefault(); e.stopPropagation(); }, false);
    });
    dz.addEventListener('dragenter', () => dz.classList.add('drop-zone-active'));
    dz.addEventListener('dragover', () => dz.classList.add('drop-zone-active'));
    dz.addEventListener('dragleave', () => dz.classList.remove('drop-zone-active'));
    dz.addEventListener('drop', (e) => {
        dz.classList.remove('drop-zone-active');
        handleFiles(e.dataTransfer.files);
    });
    dom.fileInput.addEventListener('change', (e) => handleFiles(e.target.files));
}

function handleFiles(files) {
    for (const file of files) {
        if (!file.name.match(/\.xlsx?$/i)) {
            showToast(`"${file.name}" no es un archivo Excel valido`, 'warning');
            continue;
        }
        if (!state.files.find(f => f.name === file.name)) {
            state.files.push(file);
        }
    }
    updateFileList();
}

function updateFileList() {
    const list = dom.fileList;
    list.innerHTML = '';
    if (state.files.length === 0) {
        dom.filesPreview.classList.add('hidden');
        return;
    }
    dom.filesPreview.classList.remove('hidden');
    dom.fileCount.textContent = `${state.files.length} archivo(s)`;
    const matchedKeys = new Set();
    state.files.forEach((file, index) => {
        const div = document.createElement('div');
        div.className = 'flex items-center justify-between p-2 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors animate-fade-in';
        const matchingPattern = REQUIRED_PATTERNS.find(p => p.pattern.test(file.name));
        if (matchingPattern) matchedKeys.add(matchingPattern.key);
        const iconColor = matchingPattern ? 'text-green-500' : 'text-gray-400';
        const label = matchingPattern ? matchingPattern.label : 'No identificado';
        const badgeColor = matchingPattern ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-500';
        div.innerHTML = `
            <div class="flex items-center space-x-3 min-w-0">
                <svg class="w-5 h-5 ${iconColor} flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
                </svg>
                <div class="min-w-0">
                    <p class="text-sm font-medium text-gray-700 truncate">${file.name}</p>
                    <p class="text-xs text-gray-500">${(file.size / 1024 / 1024).toFixed(1)} MB</p>
                </div>
            </div>
            <div class="flex items-center space-x-2">
                <span class="text-xs px-2 py-0.5 rounded-full ${badgeColor} whitespace-nowrap">${label}</span>
                <button onclick="removeFile(${index})" class="text-gray-400 hover:text-red-500 transition-colors">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
                    </svg>
                </button>
            </div>
        `;
        list.appendChild(div);
    });
    const missingPatterns = REQUIRED_PATTERNS.filter(p => !matchedKeys.has(p.key));
    if (missingPatterns.length > 0) {
        const missingDiv = document.createElement('div');
        missingDiv.className = 'mt-3 p-3 bg-yellow-50 border border-yellow-200 rounded-lg animate-fade-in';
        missingDiv.innerHTML = `
            <p class="text-xs font-medium text-yellow-800 mb-1">⚠️ Archivos no detectados (opcional):</p>
            <div class="flex flex-wrap gap-1">
                ${missingPatterns.map(p => `<span class="text-xs px-2 py-0.5 bg-yellow-100 text-yellow-700 rounded-full">${p.label}</span>`).join('')}
            </div>
        `;
        list.appendChild(missingDiv);
    }
    updateProcessButton();
}

function removeFile(index) {
    state.files.splice(index, 1);
    updateFileList();
}

dom.clearFilesBtn.addEventListener('click', () => {
    state.files = [];
    updateFileList();
    dom.fileInput.value = '';
});

dom.quickProcessBtn.addEventListener('click', () => {
    state.files = [{ name: '(archivos existentes en input/)', size: 0 }];
    updateFileList();
    startProcessing();
});

function updateProcessButton() {
    const hasFiles = state.files.length > 0;
    dom.processBtn.disabled = !hasFiles || state.isProcessing;
    dom.processBtnText.textContent = state.isProcessing
        ? 'PROCESANDO...'
        : hasFiles
            ? 'PROCESAR INFORME'
            : 'Primero arrastra los archivos';
}

// ======================================================================
// PROCESAMIENTO
// ======================================================================
dom.processBtn.addEventListener('click', startProcessing);

async function startProcessing() {
    if (state.isProcessing || state.files.length === 0) return;
    state.isProcessing = true;
    state.isComplete = false;
    state.isSleeping = false;
    state.completedPhaseKeys = [];
    cancelSleepTimer();
    updateProcessButton();
    dom.processIcon.classList.add('animate-spin');
    dom.processBtnText.textContent = 'SUBIR ARCHIVOS...';
    setMascotState('driving');
    showMascotThought('¡A toda velocidad! 🚗');

    try {
        // 1. SUBIR ARCHIVOS
        const formData = new FormData();
        for (const file of state.files) {
            formData.append('files[]', file);
        }
        const uploadRes = await fetch('/api/upload', {
            method: 'POST', body: formData
        });
        if (!uploadRes.ok) throw new Error('Error al subir archivos');
        const uploadData = await uploadRes.json();
        if (uploadData.errors.length > 0) {
            showToast(uploadData.errors.join(', '), 'error');
        }

        // 2. INICIAR PIPELINE (transicion de driving a rotacion)
        setTimeout(() => startMascotRotation(), 500);
        dom.processBtnText.textContent = 'PROCESANDO...';
        const month = dom.selectMonth.value;
        const year = dom.selectYear.value;
        const processRes = await fetch('/api/process', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ month, year })
        });
        if (!processRes.ok) {
            const err = await processRes.json();
            throw new Error(err.error || 'Error al iniciar proceso');
        }

        showPipeline();
        connectSSE();
    } catch (error) {
        handleError(error.message);
    }
}

// ======================================================================
// SSE
// ======================================================================
function connectSSE() {
    if (state.eventSource) state.eventSource.close();
    state.eventSource = new EventSource('/api/events');
    state.eventSource.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);
            if (data.type === 'progress') updatePipeline(data);
            else if (data.type === 'done') onProcessingComplete(data.phase === 'completed');
            else if (data.type === 'error') handleError(data.message);
        } catch (e) { console.error('SSE parse error:', e); }
    };
    state.eventSource.onerror = () => {
        if (state.eventSource) { state.eventSource.close(); state.eventSource = null; }
        pollStatus();
    };
}

function pollStatus() {
    const interval = setInterval(async () => {
        try {
            const res = await fetch('/api/status');
            const status = await res.json();
            if (status.phase === 'completed' || status.phase === 'error') {
                clearInterval(interval);
                onProcessingComplete(status.phase === 'completed');
                return;
            }
            if (status.events && status.events.length > 0) {
                const lastEvent = status.events[status.events.length - 1];
                updatePipeline({
                    phase: lastEvent.phase,
                    message: lastEvent.message,
                    progress: lastEvent.progress,
                    detail: lastEvent.detail,
                    status: lastEvent.status
                });
            }
        } catch (e) { console.error('Poll error:', e); }
    }, 500);
}

// ======================================================================
// TIMER
// ======================================================================
let processTimer = null;
let processStartTime = null;

function startTimer() {
    processStartTime = Date.now();
    if (processTimer) clearInterval(processTimer);
    processTimer = setInterval(() => {
        if (!processStartTime) return;
        const elapsed = Math.floor((Date.now() - processStartTime) / 1000);
        const min = Math.floor(elapsed / 60);
        const sec = elapsed % 60;
        document.title = `[${dom.progressPercent.textContent}] SDG — ${min}:${sec.toString().padStart(2, '0')}`;
    }, 1000);
}

function stopTimer() {
    if (processTimer) { clearInterval(processTimer); processTimer = null; }
    document.title = 'SDG Localidades — Sistema de Informes PQRS';
}

// ======================================================================
// PIPELINE VISUAL
// ======================================================================

function showPipeline() {
    dom.pipelineContainer.classList.remove('hidden');
    dom.resultContainer.classList.add('hidden');
    dom.completedPhases.innerHTML = '';
    dom.pendingPhases.innerHTML = '';
    dom.pipelineTitle.textContent = 'Procesando informe...';
    dom.pipelineStatusDot.className = 'w-3 h-3 bg-blue-500 rounded-full mr-2 animate-pulse';

    // Crear fases en pendingPhases
    const orderedPhases = Object.entries(state.phases)
        .sort(([, a], [, b]) => a.order - b.order)
        .filter(([key]) => key !== 'idle' && key !== 'completed' && key !== 'error');

    orderedPhases.forEach(([phaseKey, phase]) => {
        const div = document.createElement('div');
        div.id = `phase-${phaseKey}`;
        div.className = 'phase-item flex items-center space-x-3 p-2 rounded-lg';
        div.innerHTML = `
            <span class="phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold">○</span>
            <div class="flex-1">
                <p class="text-sm font-medium text-gray-600">${phase.label}</p>
                <p class="phase-detail text-xs text-gray-400 hidden">Esperando...</p>
            </div>
            <span class="phase-status text-xs text-gray-400">—</span>
        `;
        dom.pendingPhases.appendChild(div);
    });

    // Animacion secuencial de entrada
    document.querySelectorAll('#pendingPhases .phase-item').forEach((el, i) => {
        setTimeout(() => el.classList.add('visible'), 100 + i * 60);
    });

    addLog('🔄 Iniciando proceso de generacion de informe...');
    startTimer();
}

function updatePipeline(data) {
    // Detectar sub-fases (validation_l1..l4 desde backend via detail)
    let effectivePhase = data.phase;
    if (data.detail && data.detail.startsWith('sub_phase:')) {
        effectivePhase = data.detail.replace('sub_phase:', '');
    }

    const phase = effectivePhase;
    const message = data.message || '';
    const progress = data.progress || 0;
    const detail = data.detail || '';
    const status = data.status || 'running';

    // Actualizar barra
    dom.progressBar.style.width = `${Math.round(progress * 100)}%`;
    dom.progressPercent.textContent = `${Math.round(progress * 100)}%`;
    dom.progressLabel.textContent = message;
    if (progress > 0.85) dom.progressBar.classList.add('progress-animated');

    // Mascota: rotacion de 3 estados + estados especiales
    const mappedState = MASCOT_STATES[phase] || (phase.startsWith('validation_') ? 'repairing' : null);
    if (mappedState === 'repairing' || mappedState === 'driving') {
        // Estados especiales: detener rotacion, mostrar estado concreto
        stopMascotRotation();
        setMascotState(mappedState);
        const thought = MASCOT_THOUGHTS[mappedState] || (phase.startsWith('validation_l') ? 'Validando...' : '');
        showMascotThought(thought);
    } else if (mappedState === 'reading' || mappedState === 'analyzing' || mappedState === 'watching') {
        // Estados rotativos: iniciar o continuar rotacion
        if (!state._rotationTimer) {
            startMascotRotation();
        }
    } else if (!state._rotationTimer) {
        // Fallback: idle si no hay rotacion ni estado especial
        setMascotState('idle');
        showMascotThought('');
    }

    // Manejar fases de validacion (validation_l1..l4)
    const isValidationSub = phase.startsWith('validation_l');

    // Determinar el indice de la fase actual
    const orderedKeys = Object.keys(state.phases)
        .filter(k => k !== 'idle' && k !== 'completed' && k !== 'error')
        .sort((a, b) => state.phases[a].order - state.phases[b].order);

    // Si es sub-fase de validacion, NO marcar validation como completada aun
    // Encontrar que fase padre estamos
    let currentPhaseKey = phase;
    if (isValidationSub) {
        // Mostrar detalle en validation
        const vEl = document.getElementById('phase-validation');
        if (vEl) {
            const detailEl = vEl.querySelector('.phase-detail');
            if (detailEl) {
                detailEl.classList.remove('hidden');
                detailEl.textContent = message || 'Validando...';
            }
        }
        // Marcar sub-fase como running
        const subEl = document.getElementById(`phase-${phase}`);
        if (subEl) {
            subEl.classList.remove('pending','completed','running','error');
            subEl.classList.add('running');
            const icon = subEl.querySelector('.phase-icon');
            icon.textContent = '⟳';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-blue-600 animate-spin';
            const st = subEl.querySelector('.phase-status');
            st.textContent = '⟳';
            st.className = 'phase-status text-xs text-blue-600';
        }
        // Las sub-fases anteriores de validacion deben marcarse completadas
        const vSubKeys = orderedKeys.filter(k => k.startsWith('validation_l'));
        const currentIdx = vSubKeys.indexOf(phase);
        for (let i = 0; i < currentIdx; i++) {
            const pastKey = vSubKeys[i];
            movePhaseToCompleted(pastKey);
        }
        // Actualizar progreso
        if (status === 'completed') {
            movePhaseToCompleted(phase);
            // Si todas las 4 sub-fases estan completas, marcar validation como completada
            const allDone = vSubKeys.every(k =>
                document.getElementById(`phase-${k}`) === null ||
                document.getElementById(`phase-${k}`)?.closest('#completedPhases')
            );
            if (allDone) {
                setTimeout(() => movePhaseToCompleted('validation'), 300);
            }
        }
        return;
    }

    // Fases normales (no sub-fases de validacion)
    if (phase === 'validation') {
        // Si validation llega y hay sub-fases, mostrar las 4 sub-fases
        const vSubKeys = orderedKeys.filter(k => k.startsWith('validation_l'));
        vSubKeys.forEach(k => {
            if (!document.getElementById(`phase-${k}`)) {
                const p = state.phases[k];
                const div = document.createElement('div');
                div.id = `phase-${k}`;
                div.className = 'phase-item flex items-center space-x-3 p-2 rounded-lg ml-6';
                div.innerHTML = `
                    <span class="phase-icon w-5 h-5 flex items-center justify-center text-xs font-bold border border-gray-300 rounded-full">${p.icon}</span>
                    <div class="flex-1">
                        <p class="text-sm text-gray-600">${p.label}</p>
                        <p class="phase-detail text-xs text-gray-400 hidden">Esperando...</p>
                    </div>
                    <span class="phase-status text-xs text-gray-400">—</span>
                `;
                dom.pendingPhases.appendChild(div);
                setTimeout(() => div.classList.add('visible'), 50);
            }
        });
    }

    // Calcular indice actual
    let currentIndex = orderedKeys.indexOf(currentPhaseKey);
    if (currentIndex === -1) currentIndex = orderedKeys.length;

    orderedKeys.forEach((phaseKey, index) => {
        if (phaseKey.startsWith('validation_l')) return; // sub-fases manejadas arriba
        const el = document.getElementById(`phase-${phaseKey}`);
        if (!el) return;

        // Si ya esta en completed, no tocar
        if (el.closest('#completedPhases')) return;

        if (index < currentIndex) {
            movePhaseToCompleted(phaseKey);
        } else if (index === currentIndex) {
            el.classList.remove('completed', 'running', 'error', 'pending');
            el.classList.add('running');
            const icon = el.querySelector('.phase-icon');
            icon.textContent = '⟳';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-blue-600 animate-spin';
            const statusText = el.querySelector('.phase-status');
            statusText.textContent = status === 'completed' ? '✅' : '⟳';
            statusText.className = `phase-status text-xs ${status === 'error' ? 'text-red-600' : 'text-blue-600'}`;
            const detailEl = el.querySelector('.phase-detail');
            detailEl.classList.remove('hidden');
            detailEl.textContent = message;
        }
        // Pending: mantener como esta
    });

    // Log
    if (message && status !== 'running') {
        addLog(message, status === 'error' ? 'error' : 'info');
    }
}

function movePhaseToCompleted(phaseKey) {
    const el = document.getElementById(`phase-${phaseKey}`);
    if (!el) return;
    // Si ya esta en completed, salir
    if (el.closest('#completedPhases')) return;
    if (state.completedPhaseKeys.includes(phaseKey)) return;
    state.completedPhaseKeys.push(phaseKey);

    // Animar salida
    el.classList.add('phase-slide-out');
    setTimeout(() => {
        el.classList.add('slide-complete');
        setTimeout(() => {
            // Cambiar icono a check y mover a completed
            el.classList.remove('phase-slide-out', 'slide-complete', 'running', 'pending', 'error');
            el.classList.add('completed');
            const icon = el.querySelector('.phase-icon');
            icon.textContent = '✓';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-green-600';
            const statusText = el.querySelector('.phase-status');
            statusText.textContent = '✅';
            statusText.className = 'phase-status text-xs text-green-600';
            const detailEl = el.querySelector('.phase-detail');
            detailEl.classList.remove('hidden');
            detailEl.textContent = 'Completado';

            // Mover a completedPhases
            dom.completedPhases.appendChild(el);
            el.style.opacity = '0.8';
            el.style.transform = 'scale(0.97)';

            // Animar pendientes restantes para que suban
            document.querySelectorAll('#pendingPhases .phase-item').forEach((pendEl, i) => {
                setTimeout(() => {
                    pendEl.classList.add('shift-up');
                    setTimeout(() => pendEl.classList.remove('shift-up'), 400);
                }, i * 50);
            });
        }, 300);
    }, 200);
}

function addLog(message, type = 'info') {
    const log = dom.detailLog;
    const time = new Date().toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const colors = { info: 'text-gray-600', error: 'text-red-600', warning: 'text-yellow-600', success: 'text-green-600' };
    const div = document.createElement('div');
    div.className = `text-sm ${colors[type] || colors.info} animate-slide-in`;
    div.innerHTML = `<span class="text-gray-400">[${time}]</span> ${message}`;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
}

// ======================================================================
// COMPLETADO / ERROR
// ======================================================================

function onProcessingComplete(success) {
    state.isProcessing = false;
    state.isComplete = success;
    state.isSleeping = false;
    cancelSleepTimer();
    stopTimer();

    // Detener animacion del boton
    dom.processIcon.classList.remove('animate-spin');
    dom.processBtn.disabled = false;
    dom.processBtnText.textContent = 'PROCESAR INFORME';

    if (state.eventSource) { state.eventSource.close(); state.eventSource = null; }

    dom.pipelineStatusDot.className = success
        ? 'w-3 h-3 bg-green-500 rounded-full mr-2'
        : 'w-3 h-3 bg-red-500 rounded-full mr-2';

    dom.pipelineTitle.textContent = success
        ? '✅ ¡Proceso completado exitosamente!'
        : '❌ Error en el proceso';

    // Detener rotacion de mascota
    stopMascotRotation();

    if (success) {
        // Mascota feliz + melodia
        setMascotState('dancing');
        showMascotThought('¡Mision cumplida! 🎉');
        playCompletionMelody();
        setTimeout(() => showResult(), 800);
    } else {
        setMascotState('idle');
        showMascotThought('Algo salio mal...');
    }

    updateProcessButton();
}

function handleError(message) {
    state.isProcessing = false;
    dom.processBtn.disabled = false;
    dom.processIcon.classList.remove('animate-spin');
    dom.processBtnText.textContent = 'PROCESAR INFORME';
    addLog(`❌ ${message}`, 'error');
    dom.pipelineStatusDot.className = 'w-3 h-3 bg-red-500 rounded-full mr-2';
    dom.pipelineTitle.textContent = '❌ Error en el proceso';
    stopMascotRotation();
    setMascotState('idle');
    showMascotThought('¡Oh no! Algo salio mal...');
    showToast(message, 'error');
    updateProcessButton();
}

// ======================================================================
// RESULTADO
// ======================================================================
function showResult() {
    setTimeout(() => {
        dom.pipelineContainer.classList.add('hidden');
        dom.resultContainer.classList.remove('hidden');
        dom.resultContainer.classList.add('animate-fade-in');
        const month = dom.selectMonth.value;
        const year = dom.selectYear.value;
        const filename = `INFORME PQRS LOCALIDADES ${month} ${year}.xlsx`;
        dom.resultMessage.textContent = `El archivo ${filename} esta listo para descargar.`;
        dom.resultDetails.textContent = `Periodo: ${month} ${year} | Generado automaticamente por SDG Localidades`;
        dom.downloadBtn.href = '/api/download';
        dom.downloadBtn.download = filename;
        showToast('✅ Informe generado exitosamente', 'success');
    }, 800);
}

dom.newProcessBtn.addEventListener('click', () => {
    state.isComplete = false;
    state.completedPhaseKeys = [];
    dom.resultContainer.classList.add('hidden');
    dom.pipelineContainer.classList.add('hidden');
    dom.progressBar.style.width = '0%';
    dom.progressPercent.textContent = '0%';
    dom.detailLog.innerHTML = '<div class="text-sm text-gray-600 font-mono">Esperando inicio del proceso...</div>';
    dom.completedPhases.innerHTML = '';
    dom.pendingPhases.innerHTML = '';
    stopMascotRotation();
    setMascotState('idle');
    showMascotThought('');
});

// ======================================================================
// TOASTS
// ======================================================================
function showToast(message, type = 'info') {
    const colors = { info: 'bg-blue-500', success: 'bg-green-500', warning: 'bg-yellow-500', error: 'bg-red-500' };
    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 ${colors[type]} text-white px-6 py-3 rounded-lg shadow-lg animate-slide-in z-50 max-w-md text-sm font-medium`;
    toast.textContent = message;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s';
        setTimeout(() => toast.remove(), 500);
    }, 4000);
}

// ======================================================================
// INICIALIZACION
// ======================================================================
// ======================================================================
// TAB MANAGER — Premium Tab System with Lazy Loading
// ======================================================================
class TabManager {
    constructor() {
        this.tabs = [];
        this.activeTab = 'informe';
        this.containers = new Map();     // tabKey -> DOM container
        this.stateMap = new Map();       // tabKey -> serialized state
        this.mountHooks = new Map();     // tabKey -> fn(container, state)
        this.destroyHooks = new Map();   // tabKey -> fn(container)
        this._previousActive = 'informe';
        this._abortControllers = new Map();
        this._mountedTabs = new Set();

        this._tabBarInner = document.getElementById('tabBarInner');
        this._indicator = null;
        this._contentArea = document.getElementById('tabContentArea');
    }

    defineTabs(tabDefs) {
        // tabDefs: [{key, label, icon (svg path), iconColor}]
        this.tabs = tabDefs;
        this._renderTabBar();
        this._createIndicator();
        this._bindEvents();
    }

    _renderTabBar() {
        this._tabBarInner.innerHTML = '';
        this.tabs.forEach((tab, i) => {
            const btn = document.createElement('button');
            btn.className = `tab-bar-item${i === 0 ? ' active' : ''}`;
            btn.dataset.tab = tab.key;
            btn.innerHTML = `
                <svg class="tab-icon" style="color:${tab.iconColor || 'currentColor'}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    ${tab.icon}
                </svg>
                ${tab.label}
            `;
            this._tabBarInner.appendChild(btn);
        });
    }

    _createIndicator() {
        this._indicator = document.createElement('div');
        this._indicator.id = 'tabBarIndicator';
        this._tabBarInner.appendChild(this._indicator);
        requestAnimationFrame(() => this._updateIndicator(true));
    }

    _bindEvents() {
        this._tabBarInner.addEventListener('click', (e) => {
            const btn = e.target.closest('.tab-bar-item');
            if (!btn) return;
            const key = btn.dataset.tab;
            if (key !== this.activeTab) this.setActive(key);
        });

        // Resize observer for indicator
        if (window.ResizeObserver) {
            const ro = new ResizeObserver(() => this._updateIndicator(true));
            ro.observe(this._tabBarInner);
        }
    }

    _updateIndicator(instant = false) {
        const active = this._tabBarInner.querySelector('.tab-bar-item.active');
        if (!active || !this._indicator) return;
        const parent = this._tabBarInner;
        const pRect = parent.getBoundingClientRect();
        const aRect = active.getBoundingClientRect();
        const left = aRect.left - pRect.left + parent.scrollLeft;
        const width = aRect.width;

        if (instant) {
            this._indicator.style.transition = 'none';
            this._indicator.style.transform = `translateX(${left}px)`;
            this._indicator.style.width = `${width}px`;
            requestAnimationFrame(() => { this._indicator.style.transition = ''; });
        } else {
            this._indicator.style.transform = `translateX(${left}px)`;
            this._indicator.style.width = `${width}px`;
        }
    }

    onMount(tabKey, fn) { this.mountHooks.set(tabKey, fn); }
    onDestroy(tabKey, fn) { this.destroyHooks.set(tabKey, fn); }
    saveState(tabKey, state) { this.stateMap.set(tabKey, state); }
    restoreState(tabKey) { return this.stateMap.get(tabKey) || null; }
    getActive() { return this.activeTab; }

    setActive(tabKey) {
        if (tabKey === this.activeTab) return;

        // SSSSSSE Guard: save EventSource state before leaving INFORME
        if (this.activeTab === 'informe' && sseGuard) {
            sseGuard.save();
        }

        this._previousActive = this.activeTab;

        // ── Destroy current tab ──
        if (this._previousActive !== 'informe') {
            // Save state before destroy
            const prevContainer = document.getElementById(`tab-${this._previousActive}`);
            if (prevContainer && !prevContainer.closest('template')) {
                const inputs = prevContainer.querySelectorAll('input, textarea, select');
                const state = {};
                inputs.forEach(el => { if (el.name) state[el.name] = el.value; });
                this.saveState(this._previousActive, state);
                prevContainer.scrollTop = 0;
            }

            // Run destroy hooks
            if (this.destroyHooks.has(this._previousActive)) {
                this.destroyHooks.get(this._previousActive)(prevContainer);
            }

            // Abort pending operations
            if (this._abortControllers.has(this._previousActive)) {
                this._abortControllers.get(this._previousActive).abort();
                this._abortControllers.delete(this._previousActive);
            }

            // Destroy DOM
            const prevPanel = document.getElementById(`tab-${this._previousActive}`);
            if (prevPanel && !prevPanel.closest('template')) {
                prevPanel.remove();
            }
        } else {
            // INFORME tab: hide (don't destroy)
            const informePanel = document.getElementById('tab-informe');
            if (informePanel) {
                informePanel.classList.remove('tab-show');
                informePanel.classList.add('tab-hide');
            }
        }

        // ── Mount new tab ──
        if (tabKey === 'informe') {
            // INFORME: just show
            const informePanel = document.getElementById('tab-informe');
            if (informePanel) {
                informePanel.classList.remove('tab-hide');
                informePanel.classList.add('tab-show');
            }
            // Reconnect SSE if needed
            if (sseGuard) sseGuard.restore();
        } else {
            // New tabs: mount from template, create from scratch, or show cached
            let existing = document.getElementById(`tab-${tabKey}`);
            if (!existing) {
                // First mount: try template first, else create empty container
                const template = document.getElementById(`tab-${tabKey}`);
                if (template && template.content) {
                    const clone = template.content.cloneNode(true);
                    const panel = clone.querySelector('.tab-panel');
                    if (panel) {
                        panel.id = `tab-${tabKey}`;
                        panel.classList.add('tab-panel-active');
                        this._contentArea.appendChild(panel);
                        existing = panel;
                        this._mountedTabs.add(tabKey);
                    }
                }
                // If no template or panel found, create empty container for mount hook
                if (!existing) {
                    const container = document.createElement('div');
                    container.id = `tab-${tabKey}`;
                    container.className = 'tab-panel-active';
                    this._contentArea.appendChild(container);
                    existing = container;
                    this._mountedTabs.add(tabKey);
                }
            } else {
                // Already mounted before: show
                existing.classList.remove('tab-hide');
                existing.classList.add('tab-panel-active');
                // Restore state
                const savedState = this.restoreState(tabKey);
                if (savedState) {
                    Object.entries(savedState).forEach(([name, value]) => {
                        const el = existing.querySelector(`[name="${name}"]`);
                        if (el) el.value = value;
                    });
                }
            }

            // Run mount hooks
            if (existing && this.mountHooks.has(tabKey)) {
                this.mountHooks.get(tabKey)(existing, this.restoreState(tabKey));
            }

            // Create AbortController for this tab cycle
            this._abortControllers.set(tabKey, new AbortController());
        }

        // ── Update UI ──
        this.activeTab = tabKey;
        this._tabBarInner.querySelectorAll('.tab-bar-item').forEach(btn => {
            btn.classList.toggle('active', btn.dataset.tab === tabKey);
        });
        this._updateIndicator();

        // Scroll to top of tab content
        window.scrollTo({ top: this._contentArea.offsetTop - 80, behavior: 'smooth' });
    }
}

// ======================================================================
// SSE GUARD — Preserve EventSource across INFORME tab hide/show
// ======================================================================
const sseGuard = {
    _eventSource: null,
    _active: false,
    _pipelineRunning: false,
    _reconnectTimer: null,

    save() {
        // Keep reference to EventSource (don't close it)
        this._active = true;
    },

    restore() {
        if (!this._active) return;
        this._active = false;

        // If pipeline was running and EventSource exists, reconnect UI
        // (The existing EventSource continues to receive messages)
        if (state.eventSource && state.isProcessing) {
            // UI elements are back in DOM, SSE will find them
            console.debug('[SSE Guard] Reconnected to active EventSource');
        }
        // If pipeline completed, no need to reconnect
    },

    close() {
        if (state.eventSource) {
            state.eventSource.close();
            state.eventSource = null;
        }
        this._eventSource = null;
        this._active = false;
        this._pipelineRunning = false;
    },

    isActive() { return this._active; }
};

// Patch existing EventSource creation to use the guard
const _origConnectSSE = connectSSE;
connectSSE = function() {
    sseGuard._pipelineRunning = true;
    _origConnectSSE();
};

const _origOnProcessingComplete = onProcessingComplete;
onProcessingComplete = function(success) {
    sseGuard._pipelineRunning = false;
    if (!success) { sseGuard.close(); }
    _origOnProcessingComplete(success);

    // If successful, fetch dashboard data
    if (success) {
        setTimeout(() => fetchDashboard(), 1200);
    }
};

// Hook into "Nuevo informe" to hide dashboard
const _origNewProcess = dom.newProcessBtn?.click;
if (dom.newProcessBtn) {
    dom.newProcessBtn.addEventListener('click', function() {
        hideDashboard();
    });
}

// ======================================================================
// DASHBOARD PREMIUM — Chart.js + Hover Overlays + Animated Counters
// ======================================================================

// Chart.js instances registry (for cleanup)
let dashboardCharts = {};

// ─── COLORS ───
const DASH_COLORS = {
    blue:   ['#2E75B6', '#3B82F6', '#60A5FA', '#93BBF8'],
    green:  ['#10B981', '#34D399', '#6EE7B7'],
    purple: ['#8B5CF6', '#A78BFA', '#C4B5FD'],
    amber:  ['#F59E0B', '#FBBF24', '#FCD34D'],
    red:    ['#EF4444', '#F87171', '#FCA5A5'],
    teal:   ['#14B8A6', '#2DD4BF', '#5EEAD4'],
    orange: ['#F97316', '#FB923C', '#FDA96A'],
    // Dark mode variants
    darkBlue:   ['#6C5CE7', '#a29bfe', '#b8b5ff'],
    darkGreen:  ['#00b894', '#55efc4', '#81ecec'],
    darkPurple: ['#a29bfe', '#b8b5ff', '#d5ccff'],
    darkAmber:  ['#fdcb6e', '#ffeaa7', '#fff0c0'],
    darkRed:    ['#e17055', '#f8a5a5', '#fbc5c5'],
};

function isDarkMode() {
    return document.body.classList.contains('dark-mode');
}

function dashColor(paletteKey, index = 0) {
    const dark = isDarkMode();
    const palettes = {
        blue: dark ? DASH_COLORS.darkBlue : DASH_COLORS.blue,
        green: dark ? DASH_COLORS.darkGreen : DASH_COLORS.green,
        purple: dark ? DASH_COLORS.darkPurple : DASH_COLORS.purple,
        amber: dark ? DASH_COLORS.darkAmber : DASH_COLORS.amber,
        red: dark ? DASH_COLORS.darkRed : DASH_COLORS.red,
        teal: DASH_COLORS.teal,
        orange: DASH_COLORS.orange,
    };
    const p = palettes[paletteKey] || palettes.blue;
    return p[index % p.length];
}

// ─── ANIMATED COUNTER ───
function animateCounter(el, target, suffix = '', duration = 1000) {
    if (!el) return;
    const start = performance.now();
    const isFloat = target % 1 !== 0;
    const startVal = 0;

    function update(now) {
        const progress = Math.min((now - start) / duration, 1);
        // Ease out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        const current = startVal + (target - startVal) * eased;
        el.textContent = isFloat ? current.toFixed(1) : Math.round(current).toLocaleString();
        el.textContent += suffix;
        if (progress < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
}

// ─── DASHBOARD ENTRY ───
async function fetchDashboard() {
    const dashContainer = document.getElementById('dashboardContainer');
    const dashLoading = document.getElementById('dashboardLoading');
    const dashEmpty = document.getElementById('dashboardEmpty');
    const dashData = document.getElementById('dashboardData');
    if (!dashContainer) return;

    // Entrance animation
    dashContainer.classList.remove('hidden');
    dashLoading.classList.remove('hidden');
    dashEmpty.classList.add('hidden');
    dashData.classList.add('hidden');
    dashContainer.style.opacity = '0';
    dashContainer.style.transform = 'translateY(24px)';
    requestAnimationFrame(() => {
        dashContainer.style.transition = 'all 0.6s cubic-bezier(0.22, 1, 0.36, 1)';
        dashContainer.style.opacity = '1';
        dashContainer.style.transform = 'translateY(0)';
    });

    try {
        const res = await fetch('/api/dashboard');
        const data = await res.json();
        dashLoading.classList.add('hidden');

        if (!data.periodo) {
            dashEmpty.classList.remove('hidden');
            return;
        }

        dashData.classList.remove('hidden');
        renderPremiumDashboard(data);
    } catch (e) {
        dashLoading.classList.add('hidden');
        dashEmpty.classList.remove('hidden');
        const p = dashEmpty.querySelector('p');
        if (p) p.textContent = 'Error al cargar dashboard';
        console.error('Dashboard fetch error:', e);
    }
}

// ─── MAIN RENDER ───
function renderPremiumDashboard(data) {
    // Destroy existing charts
    Object.values(dashboardCharts).forEach(c => { try { c.destroy(); } catch(e) {} });
    dashboardCharts = {};

    const periodo = document.getElementById('dashboardPeriodo');
    if (periodo) periodo.textContent = `${data.periodo.month} ${data.periodo.year}`;

    renderDashboardMetrics(data);
    renderChartPqrs(data);
    renderChartDistribution(data);
    renderChartComparativa(data);
    renderChartSatisfaccion(data);
    renderDashboardAccordion(data);

    // Stagger entrance animations for chart cards
    document.querySelectorAll('.chart-card').forEach((card, i) => {
        card.style.animation = `dashChartIn 0.5s cubic-bezier(0.22, 1, 0.36, 1) forwards`;
        card.style.animationDelay = `${0.15 + i * 0.08}s`;
    });
}

// ════════════════════════════════════════════════════════════════
// 1. METRIC CARDS — con hover overlay y animacion de conteo
// ════════════════════════════════════════════════════════════════
function renderDashboardMetrics(data) {
    const grid = document.getElementById('metricCardsGrid');
    if (!grid || !data.resumen) return;
    grid.innerHTML = '';

    const metrics = [
        {
            key: 'total_pqrs', label: 'PQRS Totales', value: data.resumen.total_pqrs,
            color: '#2E75B6', bg: '#EBF5FF', iconColor: '#2E75B6',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>',
            hoverStats: data.tabs?.pqrs ? [
                { label: 'Gestionadas', value: data.tabs.pqrs.gestionadas || 0, color: '#10B981' },
                { label: 'Pendientes', value: data.tabs.pqrs.pendientes || 0, color: '#F59E0B' },
            ] : null,
            barColor: '#2E75B6', barPct: 100
        },
        {
            key: 'gestionadas', label: 'PQRS Gestionadas', value: data.resumen.gestionadas,
            color: '#10B981', bg: '#F0FFF4', iconColor: '#10B981',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>',
            hoverStats: data.resumen.total_pqrs ? [
                { label: 'Tasa de gestion', value: `${Math.round((data.resumen.gestionadas / data.resumen.total_pqrs) * 100)}%`, color: '#10B981' },
                { label: 'Meta esperada', value: '85%', color: '#6B7280' },
            ] : null,
            barColor: '#10B981',
            barPct: data.resumen.total_pqrs ? Math.round((data.resumen.gestionadas / data.resumen.total_pqrs) * 100) : 0
        },
        {
            key: 'orientaciones', label: 'Orientaciones SAC', value: data.resumen.orientaciones,
            color: '#14B8A6', bg: '#F0FFFA', iconColor: '#14B8A6',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/>',
            hoverStats: data.tabs?.atenciones ? [
                { label: 'Total atenciones', value: data.tabs.atenciones.total_sac || 0, color: '#14B8A6' },
                { label: 'Orientaciones', value: data.tabs.atenciones.orientaciones || 0, color: '#2E75B6' },
            ] : null,
            barColor: '#14B8A6',
            barPct: data.tabs?.atenciones ? Math.round(((data.tabs.atenciones.orientaciones || 0) / (data.tabs.atenciones.total_sac || 1)) * 100) : 0
        },
        {
            key: 'cert_residencia', label: 'Cert. Residencia', value: data.resumen.cert_residencia,
            color: '#F59E0B', bg: '#FFFBEB', iconColor: '#F59E0B',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438"/>',
            hoverStats: data.tabs?.cert_residencia ? [
                { label: 'Total certificados', value: data.tabs.cert_residencia.total || 0, color: '#F59E0B' },
            ] : null,
            barColor: '#F59E0B',
            barPct: data.tabs?.cert_residencia ? 100 : 0
        },
        {
            key: 'calificacion', label: 'Calificacion', value: data.resumen.calificacion,
            color: '#8B5CF6', bg: '#F5F3FF', iconColor: '#8B5CF6',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z"/>',
            hoverStats: [
                { label: 'Satisfaccion', value: `${data.resumen.satisfaccion || 85}%`, color: '#8B5CF6' },
                { label: 'Encuestas completas', value: data.resumen.encuestas_completas || 0, color: '#10B981' },
            ],
            barColor: '#8B5CF6',
            barPct: (data.resumen.calificacion / 5) * 100
        },
        {
            key: 'doc_extraviados', label: 'Doc. Extraviados', value: data.resumen.doc_extraviados,
            color: '#EF4444', bg: '#FFF0F0', iconColor: '#EF4444',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>',
            hoverStats: data.tabs?.doc_extraviados ? [
                { label: 'Registrados', value: data.tabs.doc_extraviados.registrados || 0, color: '#EF4444' },
            ] : null,
            barColor: '#EF4444',
            barPct: data.tabs?.doc_extraviados ? 100 : 0
        },
    ];

    metrics.forEach((m, idx) => {
        if ((m.value === undefined || m.value === null) && m.key !== 'calificacion') return;
        const displayVal = typeof m.value === 'number' && !Number.isInteger(m.value)
            ? m.value.toFixed(1) : (m.value || 0);

        const card = document.createElement('div');
        card.className = 'dash-metric-card dash-card-enter';
        card.style.animationDelay = `${idx * 0.06}s`;
        card.style.borderTopColor = m.color;

        // Main content
        let mainHtml = `
            <div class="metric-top">
                <div class="metric-icon" style="background:${m.bg};color:${m.iconColor}">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">${m.icon}</svg>
                </div>
            </div>
            <div class="metric-value" style="color:${m.color}">
                <span class="metric-counter" data-target="${displayVal}">0</span>
            </div>
            <div class="metric-label">${m.label}</div>
            ${m.barPct !== undefined ? `
                <div class="metric-trend" style="color:${m.barColor}">
                    <span class="w-1.5 h-1.5 rounded-full" style="background:${m.barColor}"></span>
                    ${m.barPct}%效能
                </div>
            ` : ''}
        `;

        // Hover overlay with detail cifras
        let hoverHtml = '';
        if (m.hoverStats && m.hoverStats.length > 0) {
            hoverHtml = `<div class="metric-hover-overlay">
                <div class="hover-title">${m.label} — Detalle</div>
                ${m.hoverStats.map(s => `
                    <div class="hover-stat">
                        <span class="stat-label">${s.label}</span>
                        <span class="stat-value" style="color:${s.color}">${typeof s.value === 'number' ? s.value.toLocaleString() : s.value}</span>
                    </div>
                `).join('')}
                <div class="hover-bar-container">
                    <div class="hover-bar-fill" style="width:${m.barPct || 0}%;background:${m.barColor}"></div>
                </div>
            </div>`;
        }

        card.innerHTML = mainHtml + hoverHtml;
        grid.appendChild(card);

        // Animate counter after card enters DOM
        const counterEl = card.querySelector('.metric-counter');
        if (counterEl) {
            const target = parseFloat(counterEl.dataset.target);
            setTimeout(() => {
                animateCounter(counterEl, target, '', 800);
            }, 300 + idx * 80);
        }
    });
}

// ════════════════════════════════════════════════════════════════
// 2. PQRS BAR CHART — Gestionadas / Pendientes
// ════════════════════════════════════════════════════════════════
function renderChartPqrs(data) {
    const canvas = document.getElementById('chartPqrs');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const pqrs = data.tabs?.pqrs || {};
    const labels = ['Gestionadas', 'Pendientes'];
    const values = [pqrs.gestionadas || 0, pqrs.pendientes || 0];
    const total = values.reduce((a,b) => a+b, 0);

    const badge = document.getElementById('pqrsTotalBadge');
    if (badge) badge.textContent = `${total.toLocaleString()} total`;

    const colors = [dashColor('green',0), dashColor('amber',0), dashColor('purple',0)];
    const bgColors = colors.map(c => c + '20'); // 12% opacity

    dashboardCharts.pqrs = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Cantidad',
                data: values,
                backgroundColor: bgColors,
                borderColor: colors,
                borderWidth: 2,
                borderRadius: 6,
                borderSkipped: false,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                    titleColor: isDarkMode() ? '#E0E0F0' : '#374151',
                    bodyColor: isDarkMode() ? '#C0C0D0' : '#6B7280',
                    borderColor: isDarkMode() ? '#2A2A4A' : '#E5E7EB',
                    borderWidth: 1,
                    cornerRadius: 8,
                    padding: 10,
                    callbacks: {
                        label: function(ctx) {
                            const pct = total > 0 ? ((ctx.raw / total) * 100).toFixed(1) : 0;
                            return `${ctx.raw.toLocaleString()} (${pct}%)`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: isDarkMode() ? '#1F1F35' : '#F3F4F6' },
                    ticks: { color: isDarkMode() ? '#9090B0' : '#9CA3AF' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: isDarkMode() ? '#C0C0D0' : '#6B7280', font: { weight: '500' } }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        },
        plugins: [{
            id: 'barLabels',
            afterDatasetsDraw(chart) {
                const meta = chart.getDatasetMeta(0);
                meta.data.forEach((bar, i) => {
                    if (values[i] === 0) return;
                    const pct = total > 0 ? ((values[i] / total) * 100).toFixed(1) : 0;
                    const ctx2 = chart.ctx;
                    ctx2.save();
                    ctx2.fillStyle = isDarkMode() ? '#E0E0F0' : '#374151';
                    ctx2.font = 'bold 11px Inter, sans-serif';
                    ctx2.textAlign = 'center';
                    ctx2.fillText(`${values[i].toLocaleString()}`, bar.x, bar.y - 8);
                    ctx2.fillStyle = isDarkMode() ? '#9090B0' : '#9CA3AF';
                    ctx2.font = '9px Inter, sans-serif';
                    ctx2.fillText(`${pct}%`, bar.x, bar.y + 14);
                    ctx2.restore();
                });
            }
        }]
    });
}

// ════════════════════════════════════════════════════════════════
// 3. DISTRIBUTION DOUGHNUT CHART
// ════════════════════════════════════════════════════════════════
function renderChartDistribution(data) {
    const canvas = document.getElementById('chartDistribution');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const tabData = data.tabs || {};
    const items = [
        { label: 'PQRS', value: tabData.pqrs?.total || data.resumen?.total_pqrs || 0, color: dashColor('blue',0) },
        { label: 'Atenciones', value: tabData.atenciones?.total_sac || data.resumen?.orientaciones || 0, color: dashColor('green',0) },
        { label: 'Cert. Residencia', value: tabData.cert_residencia?.total || data.resumen?.cert_residencia || 0, color: dashColor('amber',0) },
        { label: 'Prop. Horizontal', value: tabData.prop_horizontal?.total || 0, color: dashColor('purple',0) },
        { label: 'Encuestas', value: tabData.encuestas?.total_periodo || data.resumen?.encuestas_total || 0, color: dashColor('teal',0) },
        { label: 'Doc. Extraviados', value: tabData.doc_extraviados?.registrados || data.resumen?.doc_extraviados || 0, color: dashColor('red',0) },
    ].filter(i => i.value > 0);

    const total = items.reduce((a,b) => a + b.value, 0);
    const badge = document.getElementById('distTotalBadge');
    if (badge) badge.textContent = `${total.toLocaleString()} total`;

    const colors = items.map(i => i.color);
    const hoverColors = items.map(i => i.color + 'CC');

    dashboardCharts.distribution = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: items.map(i => i.label),
            datasets: [{
                data: items.map(i => i.value),
                backgroundColor: colors,
                hoverBackgroundColor: hoverColors,
                borderWidth: 3,
                borderColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                hoverOffset: 12,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            cutout: '55%',
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        color: isDarkMode() ? '#C0C0D0' : '#6B7280',
                        font: { size: 10, weight: '500' },
                        padding: 12,
                        boxWidth: 10,
                        usePointStyle: true,
                    }
                },
                tooltip: {
                    backgroundColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                    titleColor: isDarkMode() ? '#E0E0F0' : '#374151',
                    bodyColor: isDarkMode() ? '#C0C0D0' : '#6B7280',
                    borderColor: isDarkMode() ? '#2A2A4A' : '#E5E7EB',
                    borderWidth: 1,
                    cornerRadius: 8,
                    padding: 10,
                    callbacks: {
                        label: function(ctx) {
                            const pct = total > 0 ? ((ctx.raw / total) * 100).toFixed(1) : 0;
                            return `${ctx.label}: ${ctx.raw.toLocaleString()} (${pct}%)`;
                        }
                    }
                }
            },
            animation: {
                animateRotate: true,
                duration: 1200,
                easing: 'easeOutQuart'
            }
        },
        plugins: [{
            id: 'centerText',
            beforeDraw(chart) {
                const { width, height, ctx: c } = chart;
                c.save();
                c.textAlign = 'center';
                c.textBaseline = 'middle';
                c.fillStyle = isDarkMode() ? '#E0E0F0' : '#374151';
                c.font = 'bold 22px Inter, sans-serif';
                c.fillText(total.toLocaleString(), width/2, height/2 - 6);
                c.fillStyle = isDarkMode() ? '#9090B0' : '#9CA3AF';
                c.font = '10px Inter, sans-serif';
                c.fillText('Total', width/2, height/2 + 16);
                c.restore();
            }
        }]
    });
}

// ════════════════════════════════════════════════════════════════
// 4. COMPARATIVA — Horizontal Bar Chart
// ════════════════════════════════════════════════════════════════
function renderChartComparativa(data) {
    const canvas = document.getElementById('chartComparativa');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    const tabData = data.tabs || {};
    const items = [
        { label: 'PQRS', value: tabData.pqrs?.total || data.resumen?.total_pqrs || 0, color: dashColor('blue',0) },
        { label: 'Atenciones SAC', value: tabData.atenciones?.total_sac || data.resumen?.orientaciones || 0, color: dashColor('green',0) },
        { label: 'Cert. Residencia', value: tabData.cert_residencia?.total || data.resumen?.cert_residencia || 0, color: dashColor('amber',0) },
        { label: 'Prop. Horizontal', value: tabData.prop_horizontal?.total || 0, color: dashColor('purple',0) },
        { label: 'Encuestas', value: tabData.encuestas?.total_periodo || data.resumen?.encuestas_total || 0, color: dashColor('teal',0) },
        { label: 'Doc. Extraviados', value: tabData.doc_extraviados?.registrados || data.resumen?.doc_extraviados || 0, color: dashColor('red',0) },
    ].filter(i => i.value > 0);

    const maxVal = Math.max(...items.map(i => i.value), 1);

    dashboardCharts.comparativa = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: items.map(i => i.label),
            datasets: [{
                label: 'Volumen',
                data: items.map(i => i.value),
                backgroundColor: items.map(i => i.color + '25'),
                borderColor: items.map(i => i.color),
                borderWidth: 2,
                borderRadius: 6,
                borderSkipped: false,
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                    titleColor: isDarkMode() ? '#E0E0F0' : '#374151',
                    bodyColor: isDarkMode() ? '#C0C0D0' : '#6B7280',
                    borderColor: isDarkMode() ? '#2A2A4A' : '#E5E7EB',
                    borderWidth: 1,
                    cornerRadius: 8,
                    padding: 10,
                    callbacks: {
                        label: function(ctx) {
                            const pct = maxVal > 0 ? ((ctx.raw / maxVal) * 100).toFixed(1) : 0;
                            return `${ctx.raw.toLocaleString()} (${pct}% del maximo)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: { color: isDarkMode() ? '#1F1F35' : '#F3F4F6' },
                    ticks: { color: isDarkMode() ? '#9090B0' : '#9CA3AF' }
                },
                y: {
                    grid: { display: false },
                    ticks: { color: isDarkMode() ? '#C0C0D0' : '#6B7280', font: { weight: '500' } }
                }
            },
            animation: {
                duration: 1000,
                easing: 'easeOutQuart'
            }
        },
        plugins: [{
            id: 'endLabels',
            afterDatasetsDraw(chart) {
                const meta = chart.getDatasetMeta(0);
                meta.data.forEach((bar, i) => {
                    if (items[i].value === 0) return;
                    const c = chart.ctx;
                    c.save();
                    c.fillStyle = isDarkMode() ? '#E0E0F0' : '#374151';
                    c.font = 'bold 11px Inter, sans-serif';
                    c.textAlign = 'left';
                    c.textBaseline = 'middle';
                    c.fillText(items[i].value.toLocaleString(), bar.x + 8, bar.y);
                    c.restore();
                });
            }
        }]
    });
}

// ════════════════════════════════════════════════════════════════
// 5. SATISFACCION GAUGE + RESPUESTA RATE
// ════════════════════════════════════════════════════════════════
function renderChartSatisfaccion(data) {
    const calif = data.resumen?.calificacion || 0;
    const satisfaccion = data.resumen?.satisfaccion || 85;
    const completePct = data.resumen?.encuestas_total > 0
        ? Math.round((data.resumen.encuestas_completas / data.resumen.encuestas_total) * 100)
        : 0;

    // Satisfaction gauge
    const canvas1 = document.getElementById('chartSatisfaccion');
    if (canvas1) {
        const ctx1 = canvas1.getContext('2d');
        const satColor = calif >= 4 ? dashColor('green',0) : calif >= 3 ? dashColor('amber',0) : dashColor('red',0);

        dashboardCharts.satisfaccion = new Chart(ctx1, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [calif, 5 - calif],
                    backgroundColor: [satColor, isDarkMode() ? '#1F1F35' : '#F3F4F6'],
                    borderWidth: 0,
                    borderRadius: 4,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                cutout: '75%',
                circumference: 270,
                rotation: 225,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                        borderColor: isDarkMode() ? '#2A2A4A' : '#E5E7EB',
                        borderWidth: 1,
                        cornerRadius: 8,
                        padding: 10,
                        callbacks: {
                            label: function(ctx) {
                                return ctx.dataIndex === 0 ? `Calificacion: ${calif.toFixed(1)} / 5.0` : '';
                            }
                        }
                    }
                },
                animation: {
                    duration: 1200,
                    easing: 'easeOutQuart'
                }
            },
            plugins: [{
                id: 'gaugeCenterText',
                beforeDraw(chart) {
                    const { width, height, ctx: c } = chart;
                    c.save();
                    c.textAlign = 'center';
                    c.textBaseline = 'middle';
                    c.fillStyle = satColor;
                    c.font = 'bold 24px Inter, sans-serif';
                    c.fillText(calif.toFixed(1), width/2, height/2 - 6);
                    c.fillStyle = isDarkMode() ? '#9090B0' : '#9CA3AF';
                    c.font = '10px Inter, sans-serif';
                    c.fillText('/ 5.0', width/2, height/2 + 18);
                    c.fillStyle = isDarkMode() ? '#9090B0' : '#9CA3AF';
                    c.font = 'bold 9px Inter, sans-serif';
                    c.fillText('Calificacion', width/2, height/2 + 34);
                    c.restore();
                }
            }]
        });
    }

    // Response rate gauge
    const canvas2 = document.getElementById('chartRespuesta');
    if (canvas2) {
        const ctx2 = canvas2.getContext('2d');
        const respColor = completePct >= 80 ? dashColor('green',0) : completePct >= 50 ? dashColor('amber',0) : dashColor('red',0);

        dashboardCharts.respuesta = new Chart(ctx2, {
            type: 'doughnut',
            data: {
                datasets: [{
                    data: [completePct, 100 - completePct],
                    backgroundColor: [respColor, isDarkMode() ? '#1F1F35' : '#F3F4F6'],
                    borderWidth: 0,
                    borderRadius: 4,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: true,
                cutout: '75%',
                circumference: 270,
                rotation: 225,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: isDarkMode() ? '#1A1A2E' : '#FFFFFF',
                        borderColor: isDarkMode() ? '#2A2A4A' : '#E5E7EB',
                        borderWidth: 1,
                        cornerRadius: 8,
                        padding: 10,
                        callbacks: {
                            label: function(ctx) {
                                return ctx.dataIndex === 0 ? `Tasa de respuesta: ${completePct}%` : '';
                            }
                        }
                    }
                },
                animation: {
                    duration: 1200,
                    easing: 'easeOutQuart'
                }
            },
            plugins: [{
                id: 'gaugeCenterText2',
                beforeDraw(chart) {
                    const { width, height, ctx: c } = chart;
                    c.save();
                    c.textAlign = 'center';
                    c.textBaseline = 'middle';
                    c.fillStyle = respColor;
                    c.font = 'bold 24px Inter, sans-serif';
                    c.fillText(`${completePct}%`, width/2, height/2 - 6);
                    c.fillStyle = isDarkMode() ? '#9090B0' : '#9CA3AF';
                    c.font = 'bold 9px Inter, sans-serif';
                    c.fillText('Respuestas', width/2, height/2 + 18);
                    c.restore();
                }
            }]
        });
    }
}

// ════════════════════════════════════════════════════════════════
// 6. ACCORDION — Detail sections (enhanced)
// ════════════════════════════════════════════════════════════════
function renderDashboardAccordion(data) {
    const container = document.getElementById('dashboardAccordion');
    if (!container) return;
    container.innerHTML = '';

    const tabData = data.tabs;
    if (!tabData) return;

    const sections = [
        {
            key: 'pqrs', label: 'PQRS',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>',
            color: dashColor('blue',0), bg: isDarkMode() ? '#1A1A3E' : '#EBF5FF'
        },
        {
            key: 'atenciones', label: 'Atenciones SAC',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857"/>',
            color: dashColor('green',0), bg: isDarkMode() ? '#0A2E1A' : '#F0FFF4'
        },
        {
            key: 'cert_residencia', label: 'Cert. Residencia',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138"/>',
            color: dashColor('amber',0), bg: isDarkMode() ? '#2E1A0A' : '#FFFBEB'
        },
        {
            key: 'prop_horizontal', label: 'Prop. Horizontal',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>',
            color: dashColor('purple',0), bg: isDarkMode() ? '#1A0A2E' : '#F5F3FF'
        },
        {
            key: 'encuestas', label: 'Encuestas',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>',
            color: dashColor('teal',0), bg: isDarkMode() ? '#0A2E2A' : '#F0FFFA'
        },
        {
            key: 'doc_extraviados', label: 'Doc. Extraviados',
            icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-2.694-.833-3.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"/>',
            color: dashColor('red',0), bg: isDarkMode() ? '#2E0A0A' : '#FFF0F0'
        },
    ];

    sections.forEach(section => {
        const sData = tabData[section.key];
        if (!sData) return;

        const header = document.createElement('div');
        header.className = 'dashboard-accordion-header';
        header.innerHTML = `
            <div class="flex items-center gap-2">
                <div style="width:1.5rem;height:1.5rem;border-radius:0.375rem;background:${section.bg};color:${section.color};display:flex;align-items:center;justify-content:center">
                    <svg width="12" height="12" fill="none" stroke="currentColor" viewBox="0 0 24 24">${section.icon}</svg>
                </div>
                <span class="text-sm font-semibold text-gray-700 dark:text-gray-300">${section.label}</span>
            </div>
            <div class="flex items-center gap-3">
                <span class="text-xs font-bold" style="color:${section.color}">
                    ${(() => {
                        if (section.key === 'pqrs') return (sData.total || 0).toLocaleString();
                        if (section.key === 'atenciones') return (sData.total_sac || 0).toLocaleString();
                        if (section.key === 'cert_residencia') return (sData.total || 0).toLocaleString();
                        if (section.key === 'prop_horizontal') return (sData.total || 0).toLocaleString();
                        if (section.key === 'encuestas') return (sData.total_periodo || 0).toLocaleString();
                        if (section.key === 'doc_extraviados') return (sData.registrados || 0).toLocaleString();
                        return '0';
                    })()} registros
                </span>
                <svg class="accordion-arrow" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
                </svg>
            </div>
        `;

        const body = document.createElement('div');
        body.className = 'dashboard-accordion-body';

        if (section.key === 'pqrs') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.total || 0).toLocaleString()}</div><div class="card-label">Total PQRS</div></div>
                <div class="dashboard-card"><div class="card-value" style="color:#10B981;font-size:1.25rem">${(sData.gestionadas || 0).toLocaleString()}</div><div class="card-label">Gestionadas</div></div>
                <div class="dashboard-card"><div class="card-value" style="color:#F59E0B;font-size:1.25rem">${(sData.pendientes || 0).toLocaleString()}</div><div class="card-label">Pendientes</div></div>
            </div>`;
        } else if (section.key === 'atenciones') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.total_sac || 0).toLocaleString()}</div><div class="card-label">Total Atenciones (Orientaciones)</div></div>
            </div>`;
        } else if (section.key === 'cert_residencia') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.total || 0).toLocaleString()}</div><div class="card-label">Total Certificados</div></div>
            </div>`;
        } else if (section.key === 'prop_horizontal') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.total || 0).toLocaleString()}</div><div class="card-label">Total Tramites PH</div></div>
            </div>`;
        } else if (section.key === 'encuestas') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.total_periodo || 0).toLocaleString()}</div><div class="card-label">Total Periodo</div></div>
                <div class="dashboard-card"><div class="card-value" style="color:#10B981;font-size:1.25rem">${(sData.completas || 0).toLocaleString()}</div><div class="card-label">Respuestas Completas</div></div>
                <div class="dashboard-card"><div class="card-value" style="color:#F59E0B;font-size:1.25rem">${(sData.calificacion || 0).toFixed(1)}</div><div class="card-label">Calificacion</div></div>
            </div>`;
        } else if (section.key === 'doc_extraviados') {
            body.innerHTML = `<div class="dashboard-section-grid">
                <div class="dashboard-card"><div class="card-value" style="color:${section.color};font-size:1.25rem">${(sData.registrados || 0).toLocaleString()}</div><div class="card-label">Documentos Extraviados</div></div>
            </div>`;
        }

        header.addEventListener('click', () => {
            const isOpen = header.classList.toggle('open');
            body.classList.toggle('open', isOpen);
        });

        container.appendChild(header);
        container.appendChild(body);
    });
}

function hideDashboard() {
    // Destroy charts
    Object.values(dashboardCharts).forEach(c => { try { c.destroy(); } catch(e) {} });
    dashboardCharts = {};

    const dashContainer = document.getElementById('dashboardContainer');
    if (dashContainer) {
        dashContainer.classList.add('hidden');
    }
}

// ======================================================================
// TAB DASHBOARD — Mini dashboard RICO con graficas y desglose detallado
// ======================================================================
const TAB_CHARTS = {};  // registry for tab chart instances

async function renderTabDashboard(tabKey, container, dashData) {
    if (!dashData || dashData.metric_value === undefined) return;

    const ra = container.querySelector(`#ra-${tabKey}`);
    if (!ra) return;

    // Destroy existing tab chart
    if (TAB_CHARTS[tabKey]) {
        try { TAB_CHARTS[tabKey].destroy(); } catch(e) {}
        delete TAB_CHARTS[tabKey];
    }

    // Remove old dashboard if exists
    let dashEl = container.querySelector(`#td-${tabKey}`);
    if (dashEl) dashEl.remove();

    dashEl = document.createElement('div');
    dashEl.id = `td-${tabKey}`;
    dashEl.className = 'mt-4 border-t border-gray-200 dark:border-gray-700 pt-4';
    dashEl.style.animation = 'fadeIn 0.4s ease-out forwards';

    const colorMap = {
        'pqrs': { color: '#2E75B6', bg: '#EBF5FF', secondary: '#F59E0B' },
        'atenciones': { color: '#10B981', bg: '#F0FFF4' },
        'cert-residencia': { color: '#F59E0B', bg: '#FFFBEB' },
        'prop-horizontal': { color: '#8B5CF6', bg: '#F5F3FF' },
        'encuestas': { color: '#14B8A6', bg: '#F0FFFA', secondary: '#10B981' },
        'doc-extraviados': { color: '#EF4444', bg: '#FFF0F0' },
    };
    const palette = colorMap[tabKey] || { color: '#6B7280', bg: '#F3F4F6' };

    const val = dashData.metric_value || 0;
    const label = dashData.metric_label || 'Registros';
    const secVal = dashData.secondary_value;
    const secLabel = dashData.secondary_label;
    const breakdown = dashData.breakdown || {};
    const chartData = dashData.chart_data || [];
    const chartType = dashData.chart_type;

    // Build detailed stats lines from breakdown
    function buildStats(bd) {
        const entries = Object.entries(bd).filter(([k]) => !['_raw'].includes(k));
        if (entries.length === 0) return '';
        return entries.map(([k, v]) => `
            <div class="flex justify-between text-[11px] py-0.5 border-b border-gray-100 dark:border-gray-800 last:border-0">
                <span class="text-gray-500 dark:text-gray-400">${k.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())}</span>
                <span class="font-semibold" style="color:${palette.color}">${typeof v === 'number' ? v.toLocaleString() : v}${typeof v === 'number' && k.includes('tasa') ? '%' : ''}</span>
            </div>
        `).join('');
    }

    let html = `
        <div class="flex items-center gap-2 mb-3">
            <svg class="w-4 h-4" style="color:${palette.color}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/>
            </svg>
            <span class="text-xs font-bold" style="color:${palette.color}">Dashboard — ${dashData.title || tabKey.toUpperCase()}</span>
            <span class="text-[10px] text-gray-400 ml-auto truncate max-w-[180px]">${dashData.filename || ''}</span>
        </div>
        <div class="grid grid-cols-${chartData.length > 0 ? '3' : secVal !== null && secVal !== undefined ? '3' : '2'} gap-2 mb-3">
            <div class="rounded-lg p-2.5" style="background:var(--bg-card2);border:1px solid var(--border)">
                <div class="metric-value" style="color:${palette.color};font-size:1.3rem">${val.toLocaleString()}</div>
                <div class="metric-label" style="font-size:0.65rem">${label}</div>
            </div>
            <div class="rounded-lg p-2.5" style="background:var(--bg-card2);border:1px solid var(--border)">
                <div class="metric-value" style="color:${palette.color};font-size:1.3rem">${dashData.sheets || 0}</div>
                <div class="metric-label" style="font-size:0.65rem">Hojas procesadas</div>
            </div>
            ${secVal !== null && secVal !== undefined ? `
                <div class="rounded-lg p-2.5" style="background:var(--bg-card2);border:1px solid var(--border)">
                    <div class="metric-value" style="color:${tabKey === 'pqrs' ? '#F59E0B' : '#10B981'};font-size:1.1rem">${typeof secVal === 'number' ? secVal.toLocaleString() : secVal}</div>
                    <div class="metric-label" style="font-size:0.65rem">${secLabel || 'Secundario'}</div>
                </div>
            ` : ''}
        </div>
    `;

    // Add breakdown stats row
    const statsHtml = buildStats(breakdown);
    if (statsHtml) {
        html += `<div class="rounded-lg p-2.5 mb-3" style="background:var(--bg-card2);border:1px solid var(--border)">${statsHtml}</div>`;
    }

    // Add chart if chart data exists
    if (chartData.length > 0 && chartType) {
        const chartId = `tc-${tabKey}-${Date.now()}`;
        html += `<div class="relative" style="height:140px"><canvas id="${chartId}"></canvas></div>`;
        dashEl.innerHTML = html;
        ra.parentNode.insertBefore(dashEl, ra.nextSibling);

        // Render chart after DOM insertion
        setTimeout(() => {
            const canvas = document.getElementById(chartId);
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const isDark = document.body.classList.contains('dark-mode');

            if (chartType === 'doughnut') {
                TAB_CHARTS[tabKey] = new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: chartData.map(d => d.label),
                        datasets: [{
                            data: chartData.map(d => d.value),
                            backgroundColor: chartData.map(d => d.color + 'CC'),
                            borderWidth: 2,
                            borderColor: isDark ? '#1A1A2E' : '#FFFFFF',
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        cutout: '60%',
                        plugins: {
                            legend: { position: 'bottom', labels: { color: isDark ? '#C0C0D0' : '#6B7280', font: { size: 9 }, boxWidth: 8 } },
                            tooltip: {
                                backgroundColor: isDark ? '#1A1A2E' : '#FFFFFF',
                                titleColor: isDark ? '#E0E0F0' : '#374151',
                                bodyColor: isDark ? '#C0C0D0' : '#6B7280',
                                borderColor: isDark ? '#2A2A4A' : '#E5E7EB',
                                borderWidth: 1,
                                cornerRadius: 6,
                                padding: 8,
                                callbacks: {
                                    label: function(ctx) {
                                        const total = chartData.reduce((a,b) => a + b.value, 0);
                                        const pct = total > 0 ? ((ctx.raw / total) * 100).toFixed(1) : 0;
                                        return `${ctx.label}: ${ctx.raw.toLocaleString()} (${pct}%)`;
                                    }
                                }
                            }
                        },
                        animation: { duration: 800, easing: 'easeOutQuart' }
                    }
                });
            } else if (chartType === 'bar') {
                const colors = chartData.map(d => d.color);
                TAB_CHARTS[tabKey] = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: chartData.map(d => d.label),
                        datasets: [{
                            label: 'Cantidad',
                            data: chartData.map(d => d.value),
                            backgroundColor: colors.map(c => c + '25'),
                            borderColor: colors,
                            borderWidth: 2,
                            borderRadius: 4,
                            borderSkipped: false,
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                backgroundColor: isDark ? '#1A1A2E' : '#FFFFFF',
                                titleColor: isDark ? '#E0E0F0' : '#374151',
                                bodyColor: isDark ? '#C0C0D0' : '#6B7280',
                                borderColor: isDark ? '#2A2A4A' : '#E5E7EB',
                                borderWidth: 1,
                                cornerRadius: 6,
                                padding: 8,
                            }
                        },
                        scales: {
                            y: { beginAtZero: true, grid: { color: isDark ? '#1F1F35' : '#F3F4F6' }, ticks: { color: isDark ? '#9090B0' : '#9CA3AF' } },
                            x: { grid: { display: false }, ticks: { color: isDark ? '#C0C0D0' : '#6B7280' } }
                        },
                        animation: { duration: 800, easing: 'easeOutQuart' }
                    }
                });
            }
        }, 100);
        return; // chart rendered above, exit early
    }

    dashEl.innerHTML = html;
    ra.parentNode.insertBefore(dashEl, ra.nextSibling);
}


// ======================================================================
// TAB UPLOAD HANDLER — Genera upload areas con IDs unicos por tab
// ======================================================================
const TAB_CONFIG = {
    'pqrs': {
        icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z',
        color: '#2E75B6', bg: '#EBF5FF', label: 'PQRS',
        desc: 'Peticiones, Quejas, Reclamos y Sugerencias',
        fileHint: 'BD PQRS Bogota Te Escucha'
    },
    'atenciones': {
        icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857',
        color: '#10B981', bg: '#F0FFF4', label: 'Atenciones SAC',
        desc: 'Servicio de Atencion al Ciudadano',
        fileHint: 'SAC Atencion Mayo'
    },
    'cert-residencia': {
        icon: 'M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438',
        color: '#F59E0B', bg: '#FFFBEB', label: 'Certificado de Residencia',
        desc: 'Productividad de certificados',
        fileHint: 'PRODUCTIVIDAD_CR'
    },
    'prop-horizontal': {
        icon: 'M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4',
        color: '#8B5CF6', bg: '#F5F3FF', label: 'Propiedad Horizontal',
        desc: 'Productividad de PH',
        fileHint: 'PRODUCTIVIDAD_PH'
    },
    'encuestas': {
        icon: 'M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4',
        color: '#14B8A6', bg: '#F0FFFA', label: 'Encuestas',
        desc: 'Reporte de productividad de encuestas',
        fileHint: 'PRODUCTIVIDAD ENCUESTAS'
    },
    'doc-extraviados': {
        icon: 'M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-2.694-.833-3.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z',
        color: '#DC3545', bg: '#FFF0F0', label: 'Documentos Extraviados',
        desc: 'Reporte SIDE de documentos perdidos',
        fileHint: 'Resumen SIDE'
    }
};

class TabUploadHandler {
    constructor(tabKey) {
        this.tabKey = tabKey;
        this.config = TAB_CONFIG[tabKey];
        this.files = [];
        this.container = null;
        this._pollTimer = null;
    }

    getDefaultMonth() {
        const months = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'];
        const now = new Date();
        return months[now.getMonth()];
    }

    getDefaultYear() {
        return String(new Date().getFullYear());
    }

    buildHTML() {
        const k = this.tabKey;
        const cfg = this.config;
        const defMonth = this.getDefaultMonth();
        const defYear = this.getDefaultYear();
        const months = ['ENERO','FEBRERO','MARZO','ABRIL','MAYO','JUNIO','JULIO','AGOSTO','SEPTIEMBRE','OCTUBRE','NOVIEMBRE','DICIEMBRE'];
        const monthOptions = months.map(m => `<option value="${m}" ${m === defMonth ? 'selected' : ''}>${m.charAt(0) + m.slice(1).toLowerCase()}</option>`).join('');
        return `
        <div class="tab-panel">
            <div class="bg-white dark:bg-gray-900 rounded-xl shadow-sm border border-gray-200 dark:border-gray-700 p-6 mb-6">
                <div class="flex items-center gap-3 mb-6">
                    <div class="w-10 h-10 rounded-lg flex items-center justify-center" style="background:${cfg.bg};color:${cfg.color}">
                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="${cfg.icon}"/></svg>
                    </div>
                    <div>
                        <h2 class="text-lg font-bold text-gray-800 dark:text-gray-200">${cfg.label}</h2>
                        <p class="text-sm text-gray-500 dark:text-gray-400">${cfg.desc}</p>
                    </div>
                </div>

                <!-- Month/Year Selectors (Feature 3: TAB-001) -->
                <div class="flex items-center gap-4 mb-4 p-3 rounded-lg" style="background:var(--bg-card2);border:1px solid var(--border)">
                    <div class="flex items-center gap-2">
                        <svg class="w-4 h-4" style="color:${cfg.color}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                        </svg>
                        <span class="text-xs font-medium text-gray-500 dark:text-gray-400">Periodo:</span>
                    </div>
                    <select id="sm-${k}" class="text-xs rounded-lg border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 py-1.5 px-2 focus:ring-2" style="focus:border-[${cfg.color}]">
                        ${monthOptions}
                    </select>
                    <input type="number" id="sy-${k}" value="${defYear}" min="2020" max="2100"
                           class="text-xs rounded-lg border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 py-1.5 px-2 w-20 focus:ring-2">
                </div>

                <!-- Upload Area -->
                <div id="dz-${k}" class="relative border-2 border-dashed border-gray-300 dark:border-gray-600 rounded-xl p-6 mb-4 text-center cursor-pointer transition-all duration-300 hover:border-[${cfg.color}] hover:bg-[${cfg.bg}]" style="background:transparent">
                    <div class="text-center">
                        <svg class="mx-auto w-10 h-10 text-gray-400 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"/>
                        </svg>
                        <p class="text-sm font-medium text-gray-600 dark:text-gray-400 mb-1">Arrastra el archivo ${cfg.label} aqui</p>
                        <p class="text-xs text-gray-400 mb-3">o haz clic para seleccionarlo (.xlsx)</p>
                        <p class="text-xs text-gray-400 italic">Archivo esperado: ${cfg.fileHint}</p>
                        <input type="file" id="fi-${k}" accept=".xlsx,.xls" class="hidden">
                        <button id="sf-${k}" class="inline-flex items-center px-3 py-1.5 rounded-lg text-xs font-medium text-white transition-all" style="background:${cfg.color}">
                            <svg class="w-3.5 h-3.5 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828l6.414-6.586a4 4 0 00-5.656-5.656l-6.415 6.585a6 6 0 108.486 8.486L20.5 13"/></svg>
                            Seleccionar archivo
                        </button>
                    </div>
                    <div id="fp-${k}" class="hidden mt-4 border-t border-gray-200 dark:border-gray-700 pt-4">
                        <div id="fl-${k}" class="space-y-1"></div>
                        <div class="mt-2 flex items-center justify-between">
                            <span id="fc-${k}" class="text-xs text-gray-500">0 archivos</span>
                            <button id="cf-${k}" class="text-xs text-red-500 hover:text-red-700 font-medium">Limpiar</button>
                        </div>
                    </div>
                </div>

                <!-- Process Button + Status -->
                <div class="flex items-center gap-3 mb-4">
                    <button id="pb-${k}" disabled class="inline-flex items-center px-4 py-2 rounded-lg text-xs font-bold text-white opacity-50 cursor-not-allowed transition-all" style="background:${cfg.color}">
                        <svg class="w-3.5 h-3.5 mr-1.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"/></svg>
                        Procesar
                    </button>
                    <span id="st-${k}" class="text-xs text-gray-400"></span>
                </div>

                <!-- Result Area -->
                <div id="ra-${k}" class="hidden p-4 bg-green-50 dark:bg-green-900/10 border border-green-200 dark:border-green-800 rounded-lg">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-2">
                            <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            <span class="text-sm font-medium text-green-800 dark:text-green-300" id="rm-${k}">Informe generado</span>
                        </div>
                        <a id="dl-${k}" class="inline-flex items-center px-3 py-1.5 rounded-lg text-xs font-bold text-white transition-all" style="background:${cfg.color}" href="#" download>
                            <svg class="w-3.5 h-3.5 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                            Descargar
                        </a>
                    </div>
                    <p class="text-xs text-green-600 dark:text-green-400 mt-2" id="rd-${k}"></p>
                </div>

                <!-- Progress Bar (renamed pg-${k} para evitar conflicto con process button pb-${k}) -->
                <div id="pr-${k}" class="hidden mt-4">
                    <div class="flex justify-between text-xs text-gray-500 mb-1">
                        <span id="pl-${k}">Procesando...</span>
                        <span id="pp-${k}">0%</span>
                    </div>
                    <div class="w-full bg-gray-200 dark:bg-gray-700 rounded-full h-2 overflow-hidden">
                        <div id="pg-${k}" class="h-full rounded-full transition-all duration-500 ease-out" style="width:0%;background:${cfg.color}"></div>
                    </div>
                </div>
            </div>
        </div>`;
    }

    setup(container) {
        this.container = container;
        const k = this.tabKey;

        const dz = container.querySelector(`#dz-${k}`);
        const fi = container.querySelector(`#fi-${k}`);
        const sf = container.querySelector(`#sf-${k}`);
        const cf = container.querySelector(`#cf-${k}`);
        const pb = container.querySelector(`#pb-${k}`);
        const dl = container.querySelector(`#dl-${k}`);

        if (!dz) return;

        // Select files button
        sf.addEventListener('click', (e) => { e.stopPropagation(); fi.click(); });
        dz.addEventListener('click', () => fi.click());

        // Drag and drop
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(ev => {
            dz.addEventListener(ev, (e) => { e.preventDefault(); e.stopPropagation(); }, false);
        });
        dz.addEventListener('dragenter', () => dz.style.borderColor = this.config.color);
        dz.addEventListener('dragover', () => dz.style.borderColor = this.config.color);
        dz.addEventListener('dragleave', () => dz.style.borderColor = '');
        dz.addEventListener('drop', (e) => {
            dz.style.borderColor = '';
            this.handleFiles(e.dataTransfer.files);
        });

        fi.addEventListener('change', (e) => this.handleFiles(e.target.files));
        cf.addEventListener('click', () => this.clearFiles());
        pb.addEventListener('click', () => this.process());
    }

    setup(container) {
        this.container = container;
        const k = this.tabKey;

        const dz = container.querySelector(`#dz-${k}`);
        const fi = container.querySelector(`#fi-${k}`);
        const sf = container.querySelector(`#sf-${k}`);
        const cf = container.querySelector(`#cf-${k}`);
        const pb = container.querySelector(`#pb-${k}`);
        const dl = container.querySelector(`#dl-${k}`);

        if (!dz) return;

        // Select files button
        sf.addEventListener('click', (e) => { e.stopPropagation(); fi.click(); });
        dz.addEventListener('click', () => fi.click());

        // Drag and drop
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(ev => {
            dz.addEventListener(ev, (e) => { e.preventDefault(); e.stopPropagation(); }, false);
        });
        dz.addEventListener('dragenter', () => dz.style.borderColor = this.config.color);
        dz.addEventListener('dragover', () => dz.style.borderColor = this.config.color);
        dz.addEventListener('dragleave', () => dz.style.borderColor = '');
        dz.addEventListener('drop', (e) => {
            dz.style.borderColor = '';
            this.handleFiles(e.dataTransfer.files);
        });

        fi.addEventListener('change', (e) => this.handleFiles(e.target.files));
        cf.addEventListener('click', () => this.clearFiles());
        pb.addEventListener('click', () => this.process());
    }

    handleFiles(files) {
        for (const file of files) {
            if (!file.name.match(/\.xlsx?$/i)) continue;
            if (!this.files.find(f => f.name === file.name)) {
                this.files.push(file);
            }
        }
        this.updateUI();
    }

    clearFiles() {
        this.files = [];
        const k = this.tabKey;
        const fi = this.container.querySelector(`#fi-${k}`);
        if (fi) fi.value = '';
        const ra = this.container.querySelector(`#ra-${k}`);
        if (ra) ra.classList.add('hidden');
        this.updateUI();
    }

    updateUI() {
        const k = this.tabKey;
        const fp = this.container.querySelector(`#fp-${k}`);
        const fl = this.container.querySelector(`#fl-${k}`);
        const fc = this.container.querySelector(`#fc-${k}`);
        const pb = this.container.querySelector(`#pb-${k}`);
        const uploadIcon = this.container.querySelector(`#dz-${k} svg:first-of-type`);

        if (this.files.length === 0) {
            fp.classList.add('hidden');
            pb.disabled = true;
            pb.classList.add('opacity-50', 'cursor-not-allowed');
            pb.classList.remove('opacity-100', 'cursor-pointer');
            return;
        }

        fp.classList.remove('hidden');
        fl.innerHTML = '';
        fc.textContent = `${this.files.length} archivo(s)`;

        this.files.forEach((file, idx) => {
            const div = document.createElement('div');
            div.className = 'flex items-center justify-between p-1.5 rounded bg-gray-50 dark:bg-gray-800';
            div.innerHTML = `
                <span class="text-xs text-gray-600 dark:text-gray-400 truncate">${file.name}</span>
                <span class="text-xs text-gray-400">${(file.size / 1024).toFixed(0)} KB</span>
            `;
            fl.appendChild(div);
        });

        pb.disabled = false;
        pb.classList.remove('opacity-50', 'cursor-not-allowed');
        pb.classList.add('opacity-100', 'cursor-pointer');
    }

    async process() {
        const k = this.tabKey;
        if (this.files.length === 0) return;

        const pbBtn = this.container.querySelector(`#pb-${k}`);
        const st = this.container.querySelector(`#st-${k}`);
        const pr = this.container.querySelector(`#pr-${k}`);
        const pl = this.container.querySelector(`#pl-${k}`);
        const pp = this.container.querySelector(`#pp-${k}`);
        const pg = this.container.querySelector(`#pg-${k}`);
        const ra = this.container.querySelector(`#ra-${k}`);
        const rm = this.container.querySelector(`#rm-${k}`);
        const rd = this.container.querySelector(`#rd-${k}`);
        const dl = this.container.querySelector(`#dl-${k}`);

        // Get dynamic month/year from selectors (Feature 3: TAB-001)
        const monthSel = this.container.querySelector(`#sm-${k}`);
        const yearSel = this.container.querySelector(`#sy-${k}`);
        const month = monthSel ? monthSel.value : this.getDefaultMonth();
        const year = yearSel ? yearSel.value : this.getDefaultYear();

        // Show progress
        pr.classList.remove('hidden');
        pl.textContent = 'Subiendo archivo...';
        pp.textContent = '10%';
        if (pg) pg.style.width = '10%';
        pbBtn.disabled = true;

        try {
            // Upload file
            const formData = new FormData();
            formData.append('file', this.files[0]);
            const uploadRes = await fetch(`/api/tabs/${k}/upload`, { method: 'POST', body: formData });
            const uploadData = await uploadRes.json();
            if (!uploadRes.ok) throw new Error(uploadData.error || 'Error al subir');

            pp.textContent = '30%';
            pl.textContent = 'Procesando archivo...';
            if (pg) pg.style.width = '30%';

            // Start processing (async/threaded)
            const processRes = await fetch(`/api/tabs/${k}/process`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ month, year })
            });
            if (!processRes.ok) {
                const errData = await processRes.json().catch(() => ({}));
                throw new Error(errData.error || 'Error al iniciar procesamiento');
            }

            // Poll for progress (Feature 3: TAB-003)
            pl.textContent = 'Procesando...';
            const result = await this._pollProgress(k, pg, pp, pl, st);

            if (result.error) {
                throw new Error(result.error);
            }

            pp.textContent = '100%';
            pl.textContent = 'Completado';
            if (pg) pg.style.width = '100%';

            // Show result
            pr.classList.add('hidden');
            ra.classList.remove('hidden');
            rm.textContent = result.success
                ? `Informe generado: ${result.filename || ''}`
                : 'Error al procesar';
            rd.textContent = result.success
                ? `${result.rows || 0} registros en ${result.sheets || 0} hoja(s)`
                : result.error || 'Error desconocido';
            dl.href = `/api/tabs/${k}/download`;
            st.textContent = 'Completado';

            // Fetch and render tab dashboard with REAL data (Feature 2: DASH-003)
            if (result.success) {
                try {
                    const dashRes = await fetch(`/api/tabs/${k}/dashboard`);
                    const dashData = await dashRes.json();
                    if (dashData && dashData.metric_value !== undefined) {
                        renderTabDashboard(k, this.container, dashData);
                    }
                } catch (dashErr) {
                    console.warn('Tab dashboard error:', dashErr);
                }
            }

        } catch (err) {
            pl.textContent = 'Error';
            st.textContent = `Error: ${err.message}`;
            st.style.color = '#DC3545';
            // Re-enable process button on error (Juicio fix)
            pbBtn.disabled = false;
            pbBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            pbBtn.classList.add('opacity-100', 'cursor-pointer');
            setTimeout(() => pr.classList.add('hidden'), 5000);
        }
    }

    async _pollProgress(k, pg, pp, pl, st) {
        // Poll /api/tabs/${k}/status every 2s until terminal state
        const pollInterval = 2000;
        const maxPolls = 900; // 30 min max
        let polls = 0;

        return new Promise((resolve) => {
            const timer = setInterval(async () => {
                polls++;
                try {
                    const res = await fetch(`/api/tabs/${k}/status`);
                    const status = await res.json();

                    if (pg && status.progress !== undefined) {
                        const pct = Math.round(status.progress * 100);
                        pg.style.width = `${pct}%`;
                        if (pp) pp.textContent = `${pct}%`;
                    }
                    if (status.message && pl) {
                        pl.textContent = status.message;
                    }

                    // Terminal states
                    if (status.phase === 'completed') {
                        clearInterval(timer);
                        // Fetch final result
                        const dashRes = await fetch(`/api/tabs/${k}/dashboard`);
                        const dashData = await dashRes.json();
                        resolve({
                            success: true,
                            filename: status.output_file,
                            rows: dashData.metric_value || 0,
                            sheets: dashData.sheets || 0,
                            error: null
                        });
                    } else if (status.phase === 'error') {
                        clearInterval(timer);
                        resolve({ success: false, error: status.error || 'Error en procesamiento' });
                    }

                    if (polls >= maxPolls) {
                        clearInterval(timer);
                        resolve({ success: false, error: 'Tiempo de espera agotado' });
                    }
                } catch (pollErr) {
                    // Ignore poll errors, keep trying
                    if (polls >= maxPolls) {
                        clearInterval(timer);
                        resolve({ success: false, error: 'Error de conexión durante procesamiento' });
                    }
                }
            }, pollInterval);
        });
    }
}

// ======================================================================
// INITIALIZATION
// ======================================================================
document.addEventListener('DOMContentLoaded', () => {
    setupDragDrop();
    setupMascotInteraction();
    setupEyeTracking();
    setupActivityListeners();
    updateProcessButton();

    // ── Initialize Tab Manager ──
    const tabManager = new TabManager();
    window.tabManager = tabManager;

    tabManager.defineTabs([
        { key: 'informe', label: 'Informe', iconColor: '#1F4E79', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>' },
        { key: 'pqrs', label: 'PQRS', iconColor: '#2E75B6', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>' },
        { key: 'atenciones', label: 'Atenciones', iconColor: '#10B981', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857"/>' },
        { key: 'cert-residencia', label: 'Cert.Residencia', iconColor: '#F59E0B', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438"/>' },
        { key: 'prop-horizontal', label: 'Prop.Horizontal', iconColor: '#8B5CF6', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/>' },
        { key: 'encuestas', label: 'Encuestas', iconColor: '#14B8A6', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4"/>' },
        { key: 'doc-extraviados', label: 'Doc.Extraviados', iconColor: '#DC3545', icon: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4.5c-.77-.833-2.694-.833-3.464 0L3.34 16.5c-.77.833.192 2.5 1.732 2.5z"/>' },
    ]);

    // Ensure INFORME tab is visible initially
    const informePanel = document.getElementById('tab-informe');
    if (informePanel) {
        informePanel.classList.add('tab-show');
        informePanel.classList.remove('tab-hide');
    }

    // Register mount hooks for tabs — initialize upload handlers
    const tabKeys = ['pqrs', 'atenciones', 'cert-residencia', 'prop-horizontal', 'encuestas', 'doc-extraviados'];
    const tabHandlers = {};
    tabKeys.forEach(key => {
        tabManager.onMount(key, (container, state) => {
            if (!tabHandlers[key]) {
                container.innerHTML = '';
                const handler = new TabUploadHandler(key);
                container.innerHTML = handler.buildHTML();
                handler.setup(container);
                tabHandlers[key] = handler;
            }
        });
        tabManager.onDestroy(key, (container) => {
            delete tabHandlers[key];
        });
    });

    // Bounce-in al cargar la pagina
    const container = dom.mascotContainer;
    container.classList.add('mascot-bounce-in');
    setMascotState('idle');
    showMascotThought('¡Allá vooy!');

    setTimeout(() => {
        container.classList.remove('mascot-bounce-in');
        showMascotThought('');
        state._bouncedIn = true;
        resetSleepTimer();

        // Click en mascota para despertar
        container.addEventListener('click', (e) => {
            e.stopPropagation();
            if (state.isSleeping) {
                wakeUp();
            } else if (!state.isProcessing && state._bouncedIn) {
                // Mini reaccion al hacer clic despierto
                container.style.transition = 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
                container.style.transform = 'scale(1.15)';
                showMascotThought('¡Oye!');
                resetSleepTimer();
                setTimeout(() => {
                    container.style.transform = '';
                    showMascotThought('');
                }, 800);
            }
        });
    }, 2000);

    document.querySelector('header').classList.add('animate-fade-in');
    fetch('/api/status')
        .then(r => r.json())
        .then(status => {
            if (status.running) { showPipeline(); connectSSE(); }
        })
        .catch(() => {
            showToast('No se pudo conectar con el servidor', 'error');
        });
});
