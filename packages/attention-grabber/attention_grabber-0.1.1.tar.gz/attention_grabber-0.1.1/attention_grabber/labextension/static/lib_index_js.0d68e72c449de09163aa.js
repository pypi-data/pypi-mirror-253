"use strict";
(self["webpackChunkattention_grabber"] = self["webpackChunkattention_grabber"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyterlab/notebook */ "webpack/sharing/consume/default/@jupyterlab/notebook");
/* harmony import */ var _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__);

/**
 * Initialization data for the attention-grabber extension.
 */
const plugin = {
    id: 'attention-grabber:plugin',
    description: 'Flashes your screen when cells are finished, until you click on the notebook again.',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker],
    activate: (app, notebookTracker) => {
        console.log('JupyterLab extension attention-grabber is activated!');
        const audioContext = new AudioContext();
        let annoyingInterval = null;
        let grabAttentionTimeout = null;
        let isPlaying = false;
        let oscillator = null;
        let extensionEnabled = false;
        function grabAttention() {
            isPlaying = true;
            annoyingInterval = window.setInterval(toggleAnnoying, 500); // Toggle effect every 500ms
        }
        function stopAnnoying() {
            if (grabAttentionTimeout !== null) {
                clearTimeout(grabAttentionTimeout);
                grabAttentionTimeout = null;
            }
            if (annoyingInterval !== null) {
                clearInterval(annoyingInterval);
                annoyingInterval = null;
            }
            if (isPlaying) {
                toggleAnnoying(); // Ensure effect is reset
                isPlaying = false;
            }
        }
        function toggleAnnoying() {
            if (!isPlaying) {
                // Start playing tone
                oscillator = audioContext.createOscillator();
                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(440, audioContext.currentTime);
                oscillator.connect(audioContext.destination);
                oscillator.start();
                // Change screen color
                document.body.style.backgroundColor = 'red';
            }
            else {
                // Stop playing tone
                if (oscillator) {
                    oscillator.stop();
                    oscillator = null;
                }
                // Reset screen color
                document.body.style.backgroundColor = '';
            }
            isPlaying = !isPlaying;
        }
        _jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.NotebookActions.executed.connect(() => {
            if (extensionEnabled) {
                if (grabAttentionTimeout !== null) {
                    clearTimeout(grabAttentionTimeout);
                }
                grabAttentionTimeout = setTimeout(grabAttention, 3000); // Start effect 3 seconds after execution
            }
        });
        // Added toggle command
        app.commands.addCommand('toggle-attention-grabber', {
            label: 'Toggle Attention Grabber',
            execute: () => {
                extensionEnabled = !extensionEnabled;
                if (!extensionEnabled) {
                    stopAnnoying();
                }
            }
        });
        console.log('Toggle command added');
        app.contextMenu.addItem({
            command: 'toggle-attention-grabber',
            selector: '.jp-Notebook'
        });
        notebookTracker.widgetAdded.connect((tracker, notebookPanel) => {
            notebookPanel.node.addEventListener('click', stopAnnoying);
            notebookPanel.node.addEventListener('keydown', stopAnnoying);
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.0d68e72c449de09163aa.js.map