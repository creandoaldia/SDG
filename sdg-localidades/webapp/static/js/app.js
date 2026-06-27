/**
 * SDG Localidades — Frontend JavaScript
 * Maneja: drag & drop de archivos, upload, SSE events, pipeline visual, animaciones
 */

// ======================================================================
// ESTADO GLOBAL
// ======================================================================
const state = {
    files: [],              // Archivos seleccionados/subidos
    isProcessing: false,
    isComplete: false,
    currentPhase: 'idle',
    progress: 0,
    phases: {
        'idle': { label: 'Inactivo', icon: '○', order: 0 },
        'ingestion': { label: 'Lectura de archivos', icon: '📂', order: 1 },
        'normalization': { label: 'Normalización de datos', icon: '🔧', order: 2 },
        'deduplication': { label: 'Detección de duplicados', icon: '🔍', order: 3 },
        'pivot_generation': { label: 'Tablas dinámicas Q1-Q6', icon: '📊', order: 4 },
        'indicator_calculation': { label: 'Cálculo de indicadores', icon: '📈', order: 5 },
        'resumen_cifras': { label: 'Resumen de cifras', icon: '📋', order: 6 },
        'excel_generation': { label: 'Generación de Excel', icon: '📁', order: 7 },
        'validation': { label: 'Validación a 4 niveles', icon: '✅', order: 8 },
        'completed': { label: '¡Completado!', icon: '🎉', order: 9 },
        'error': { label: 'Error', icon: '❌', order: 99 },
    },
    eventSource: null
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
    pipelineContainer: document.getElementById('pipelineContainer'),
    pipelineTitle: document.getElementById('pipelineTitle'),
    pipelineStatusDot: document.getElementById('pipelineStatusDot'),
    progressBar: document.getElementById('progressBar'),
    progressLabel: document.getElementById('progressLabel'),
    progressPercent: document.getElementById('progressPercent'),
    phasesTimeline: document.getElementById('phasesTimeline'),
    detailLog: document.getElementById('detailLog'),
    resultContainer: document.getElementById('resultContainer'),
    resultMessage: document.getElementById('resultMessage'),
    resultDetails: document.getElementById('resultDetails'),
    downloadBtn: document.getElementById('downloadBtn'),
    newProcessBtn: document.getElementById('newProcessBtn'),
    selectMonth: document.getElementById('selectMonth'),
    selectYear: document.getElementById('selectYear'),
};

// ======================================================================
// ARCHIVOS REQUERIDOS (para validación)
// ======================================================================
const REQUIRED_PATTERNS = [
    { key: 'pqrs', label: 'BD PQRS Bogotá Te Escucha', pattern: /bogota.*escucha|pqrs/i },
    { key: 'sac', label: 'SAC Atención al Ciudadano', pattern: /sac_atencion/i },
    { key: 'side', label: 'Resumen SIDE', pattern: /resumen.*side/i },
    { key: 'cr', label: 'Productividad CR', pattern: /productividad.*cr/i },
    { key: 'ph', label: 'Productividad PH', pattern: /productividad.*ph/i },
    { key: 'encuestas', label: 'Reporte Encuestas', pattern: /productividad.*encuesta|encuesta.*productividad/i },
];

// ======================================================================
// FUNCIONES — DRAG & DROP
// ======================================================================
function setupDragDrop() {
    const dz = dom.dropZone;

    // Click para seleccionar archivos
    dom.selectFilesBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        dom.fileInput.click();
    });

    dz.addEventListener('click', () => dom.fileInput.click());

    // Prevenir comportamiento por defecto del browser
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dz.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    // Efectos visuales al arrastrar
    dz.addEventListener('dragenter', () => dz.classList.add('drop-zone-active'));
    dz.addEventListener('dragover', () => dz.classList.add('drop-zone-active'));
    dz.addEventListener('dragleave', () => dz.classList.remove('drop-zone-active'));
    dz.addEventListener('drop', (e) => {
        dz.classList.remove('drop-zone-active');
        const files = e.dataTransfer.files;
        handleFiles(files);
    });

    // Selección de archivos
    dom.fileInput.addEventListener('change', (e) => {
        handleFiles(e.target.files);
    });
}

function handleFiles(files) {
    for (const file of files) {
        if (!file.name.match(/\.xlsx?$/i)) {
            showToast(`"${file.name}" no es un archivo Excel válido`, 'warning');
            continue;
        }
        // Evitar duplicados
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

    // Verificar cuáles patrones están cubiertos
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
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/>
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

    // Mostrar archivos faltantes
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

// Modo rápido: procesar archivos existentes en input/
dom.quickProcessBtn = document.getElementById('quickProcessBtn');
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
// FUNCIONES — UPLOAD Y PROCESAMIENTO
// ======================================================================
dom.processBtn.addEventListener('click', startProcessing);

async function startProcessing() {
    if (state.isProcessing || state.files.length === 0) return;

    state.isProcessing = true;
    state.isComplete = false;
    updateProcessButton();

    // Animación del botón
    dom.processIcon.classList.add('animate-spin');
    dom.processBtnText.textContent = 'SUBIR ARCHIVOS...';

    try {
        // 1. SUBIR ARCHIVOS
        const formData = new FormData();
        for (const file of state.files) {
            formData.append('files[]', file);
        }

        const uploadRes = await fetch('/api/upload', {
            method: 'POST',
            body: formData
        });

        if (!uploadRes.ok) {
            throw new Error('Error al subir archivos');
        }

        const uploadData = await uploadRes.json();
        if (uploadData.errors.length > 0) {
            showToast(uploadData.errors.join(', '), 'error');
        }

        // 2. INICIAR PIPELINE
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

        // 3. MOSTRAR PIPELINE Y ESCUCHAR EVENTOS SSE
        showPipeline();

        // Conectar SSE
        connectSSE();

    } catch (error) {
        handleError(error.message);
    }
}

// ======================================================================
// SSE — SERVER-SENT EVENTS (progreso en vivo)
// ======================================================================
function connectSSE() {
    if (state.eventSource) {
        state.eventSource.close();
    }

    state.eventSource = new EventSource('/api/events');

    state.eventSource.onmessage = (event) => {
        try {
            const data = JSON.parse(event.data);

            if (data.type === 'progress') {
                updatePipeline(data);
            } else if (data.type === 'done') {
                onProcessingComplete(data.phase === 'completed');
            } else if (data.type === 'error') {
                handleError(data.message);
            }
        } catch (e) {
            console.error('SSE parse error:', e);
        }
    };

    state.eventSource.onerror = () => {
        // Fallback: polling
        if (state.eventSource) {
            state.eventSource.close();
            state.eventSource = null;
        }
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
        } catch (e) {
            console.error('Poll error:', e);
        }
    }, 500);
}

// ======================================================================
// TIMER DE PROCESO
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
        const timeStr = `${min}:${sec.toString().padStart(2, '0')}`;
        dom.progressLabel.textContent = dom.progressLabel.textContent.split(' — ')[0] + ` — ⏱ ${timeStr}`;
        // Update browser tab title
        document.title = `[${dom.progressPercent.textContent}] SDG Localidades — ${timeStr}`;
    }, 1000);
}

function stopTimer() {
    if (processTimer) {
        clearInterval(processTimer);
        processTimer = null;
    }
    document.title = 'SDG Localidades — Sistema de Informes PQRS';
}

// ======================================================================
// PIPELINE VISUAL — ANIMACIONES
// ======================================================================
function showPipeline() {
    dom.pipelineContainer.classList.remove('hidden');
    dom.resultContainer.classList.add('hidden');
    dom.pipelineTitle.textContent = 'Procesando informe...';
    dom.pipelineStatusDot.className = 'w-3 h-3 bg-blue-500 rounded-full mr-2 animate-pulse';

    // Crear timeline de fases
    const timeline = dom.phasesTimeline;
    timeline.innerHTML = '';

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
        timeline.appendChild(div);
    });

    // Pequeño delay para animación secuencial
    document.querySelectorAll('.phase-item').forEach((el, i) => {
        setTimeout(() => el.classList.add('visible'), 100 + i * 80);
    });

    addLog('🔄 Iniciando proceso de generación de informe...');
    startTimer();
}

function updatePipeline(data) {
    const phase = data.phase;
    const message = data.message || '';
    const progress = data.progress || 0;
    const detail = data.detail || '';
    const status = data.status || 'running';

    // Actualizar barra de progreso
    dom.progressBar.style.width = `${Math.round(progress * 100)}%`;
    dom.progressPercent.textContent = `${Math.round(progress * 100)}%`;
    dom.progressLabel.textContent = message;

    if (progress > 0.85) {
        dom.progressBar.classList.add('progress-animated');
    }

    // Actualizar fase actual en timeline
    const orderedPhases = Object.keys(state.phases)
        .filter(k => k !== 'idle' && k !== 'completed' && k !== 'error');

    let currentIndex = orderedPhases.indexOf(phase);
    if (currentIndex === -1) currentIndex = orderedPhases.length;

    orderedPhases.forEach((phaseKey, index) => {
        const el = document.getElementById(`phase-${phaseKey}`);
        if (!el) return;

        const icon = el.querySelector('.phase-icon');
        const statusText = el.querySelector('.phase-status');
        const detailEl = el.querySelector('.phase-detail');

        el.classList.remove('completed', 'running', 'error', 'pending');

        if (index < currentIndex) {
            // Fase completada
            el.classList.add('completed');
            icon.textContent = '✓';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-green-600';
            statusText.textContent = '✅';
            statusText.className = 'phase-status text-xs text-green-600';
            detailEl.classList.remove('hidden');
            detailEl.textContent = 'Completado';
        } else if (index === currentIndex) {
            // Fase actual
            el.classList.add('running');
            icon.textContent = '⟳';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-blue-600 animate-spin';
            statusText.textContent = status === 'completed' ? '✅' : '⟳';
            statusText.className = `phase-status text-xs ${status === 'error' ? 'text-red-600' : 'text-blue-600'}`;
            detailEl.classList.remove('hidden');
            detailEl.textContent = message;
        } else {
            // Fase pendiente
            el.classList.add('pending');
            icon.textContent = '○';
            icon.className = 'phase-icon w-6 h-6 flex items-center justify-center text-sm font-bold text-gray-400';
            statusText.textContent = '—';
            statusText.className = 'phase-status text-xs text-gray-400';
            detailEl.classList.add('hidden');
        }
    });

    // Agregar al log de detalle
    if (message && status !== 'running') {
        addLog(message, status === 'error' ? 'error' : 'info');
    }
}

function addLog(message, type = 'info') {
    const log = dom.detailLog;
    const time = new Date().toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
    const colors = {
        info: 'text-gray-600',
        error: 'text-red-600',
        warning: 'text-yellow-600',
        success: 'text-green-600'
    };

    const div = document.createElement('div');
    div.className = `text-sm ${colors[type] || colors.info} animate-slide-in`;
    div.innerHTML = `<span class="text-gray-400">[${time}]</span> ${message}`;
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
}

// ======================================================================
// COMPLETADO / ERROR
// ======================================================================
function playBeep() {
    try {
        const ctx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = ctx.createOscillator();
        osc.type = 'sine';
        osc.frequency.value = 880;
        osc.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.3);
    } catch(e) { /* fallback silencioso */ }
}

function onProcessingComplete(success) {
    state.isProcessing = false;
    state.isComplete = success;
    stopTimer();
    if (success) playBeep();

    if (state.eventSource) {
        state.eventSource.close();
        state.eventSource = null;
    }

    dom.pipelineStatusDot.className = success
        ? 'w-3 h-3 bg-green-500 rounded-full mr-2'
        : 'w-3 h-3 bg-red-500 rounded-full mr-2';

    dom.pipelineTitle.textContent = success
        ? '✅ ¡Proceso completado exitosamente!'
        : '❌ Error en el proceso';

    if (success) {
        showResult();
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

        dom.resultMessage.textContent = `El archivo ${filename} está listo para descargar.`;
        dom.resultDetails.textContent = `Periodo: ${month} ${year} | Generado automáticamente por SDG Localidades`;

        // Actualizar link de descarga
        dom.downloadBtn.href = '/api/download';
        dom.downloadBtn.download = filename;

        showToast('✅ Informe generado exitosamente', 'success');
    }, 800);
}

dom.newProcessBtn.addEventListener('click', () => {
    state.isComplete = false;
    dom.resultContainer.classList.add('hidden');
    dom.pipelineContainer.classList.add('hidden');
    dom.progressBar.style.width = '0%';
    dom.progressPercent.textContent = '0%';
    dom.detailLog.innerHTML = '<div class="text-sm text-gray-600 font-mono">Esperando inicio del proceso...</div>';
    dom.phasesTimeline.innerHTML = '';
});

// ======================================================================
// TOASTS (notificaciones)
// ======================================================================
function showToast(message, type = 'info') {
    const colors = {
        info: 'bg-blue-500',
        success: 'bg-green-500',
        warning: 'bg-yellow-500',
        error: 'bg-red-500'
    };

    const toast = document.createElement('div');
    toast.className = `fixed bottom-4 right-4 ${colors[type]} text-white px-6 py-3 rounded-lg shadow-lg 
                       animate-slide-in z-50 max-w-md text-sm font-medium`;
    toast.textContent = message;

    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.5s';
        setTimeout(() => toast.remove(), 500);
    }, 4000);
}

// ======================================================================
// INICIALIZACIÓN
// ======================================================================
document.addEventListener('DOMContentLoaded', () => {
    setupDragDrop();
    updateProcessButton();

    // Efecto de entrada para el header
    document.querySelector('header').classList.add('animate-fade-in');

    // Verificar estado del servidor al cargar
    fetch('/api/status')
        .then(r => r.json())
        .then(status => {
            if (status.running) {
                showPipeline();
                connectSSE();
            }
        })
        .catch(() => {
            showToast('No se pudo conectar con el servidor', 'error');
        });
});
