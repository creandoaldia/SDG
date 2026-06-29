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
        { el: null, cx: 44, cy: 53, baseX: 44, baseY: 53, maxD: 2.5 },
        { el: null, cx: 76, cy: 53, baseX: 76, baseY: 53, maxD: 2.5 }
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
        [44, 76].forEach((cx, i) => {
            pupils[i].setAttribute('cx', cx);
            pupils[i].setAttribute('cy', '53');
            irises[i].setAttribute('cx', cx);
            irises[i].setAttribute('cy', '53');
            if (i < 2) {
                pupils[i+2].setAttribute('cx', cx + 2);
                pupils[i+2].setAttribute('cy', '49');
            }
        });
        // Also reset the shine circles
        if (pupils.length >= 6) {
            pupils[4].setAttribute('cx', '42');
            pupils[4].setAttribute('cy', '57');
            pupils[5].setAttribute('cx', '74');
            pupils[5].setAttribute('cy', '57');
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
document.addEventListener('DOMContentLoaded', () => {
    setupDragDrop();
    setupMascotInteraction();
    setupEyeTracking();
    setupActivityListeners();
    updateProcessButton();

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
