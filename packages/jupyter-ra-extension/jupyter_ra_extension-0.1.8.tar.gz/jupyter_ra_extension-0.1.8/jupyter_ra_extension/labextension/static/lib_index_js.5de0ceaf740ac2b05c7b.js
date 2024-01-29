"use strict";
(self["webpackChunkjupyter_ra_extension"] = self["webpackChunkjupyter_ra_extension"] || []).push([["lib_index_js"],{

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
 * Initialization data for the jupyter-ra-extension extension.
 */
const plugin = {
    id: 'jupyter-ra-extension:plugin',
    description: 'Relational Algebra Symbols in Jupyter',
    autoStart: true,
    requires: [_jupyterlab_notebook__WEBPACK_IMPORTED_MODULE_0__.INotebookTracker],
    activate: (app, tracker) => {
        // send start message
        console.log('JupyterLab extension jupyter-ra-extension is activated!');
        // define helper functions
        const insertText = (text) => {
            const current = tracker.currentWidget;
            const notebook = current.content;
            const activeCell = notebook.activeCell;
            activeCell.editor.replaceSelection(text);
        };
        // register commands
        app.commands.addCommand('ratui:text1', {
            label: 'RA:',
            caption: 'Relationale Algebra',
            isEnabled: () => false,
            execute: () => { }
        });
        app.commands.addCommand('ratui:projection', {
            label: 'π',
            caption: 'Projektion:\nπ a, b (R)\nAlternativ: pi',
            execute: () => insertText('π')
        });
        app.commands.addCommand('ratui:selection', {
            label: 'σ',
            caption: 'Selektion:\nσ a=1 (R)\nAlternativ: sigma',
            execute: () => insertText('σ')
        });
        app.commands.addCommand('ratui:rename', {
            label: 'β',
            caption: 'Umbenennung:\nβ a←b (R)\nAlternativ: beta',
            execute: () => insertText('β')
        });
        app.commands.addCommand('ratui:cross', {
            label: '×',
            caption: 'Kreuzprodukt:\nR × S',
            execute: () => insertText('×')
        });
        app.commands.addCommand('ratui:join', {
            label: '⋈',
            caption: 'Natürlicher Verbund:\nR ⋈ S',
            execute: () => insertText('⋈')
        });
        app.commands.addCommand('ratui:union', {
            label: '∪',
            caption: 'Vereinigung:\nR ∪ S',
            execute: () => insertText('∪')
        });
        app.commands.addCommand('ratui:intersection', {
            label: '∩',
            caption: 'Schnitt:\nR ∩ S',
            execute: () => insertText('∩')
        });
        app.commands.addCommand('ratui:difference', {
            label: '\\',
            caption: 'Differenz:\nR \\ S',
            execute: () => insertText('\\')
        });
        app.commands.addCommand('ratui:division', {
            label: '÷',
            caption: 'Division:\nR ÷ S',
            execute: () => insertText('÷')
        });
        app.commands.addCommand('ratui:text2', {
            label: '|',
            isEnabled: () => false,
            execute: () => { }
        });
        app.commands.addCommand('ratui:arrowleft', {
            label: '←',
            caption: 'Alternativ: <-',
            execute: () => insertText('←')
        });
        app.commands.addCommand('ratui:text3', {
            label: '|',
            isEnabled: () => false,
            execute: () => { }
        });
        app.commands.addCommand('ratui:and', {
            label: '∧',
            caption: 'Alternativ: and',
            execute: () => insertText('∧')
        });
        app.commands.addCommand('ratui:or', {
            label: '∨',
            caption: 'Alternativ: or',
            execute: () => insertText('∨')
        });
        app.commands.addCommand('ratui:not', {
            label: '¬',
            caption: 'Alternativ: !',
            execute: () => insertText('¬')
        });
        app.commands.addCommand('ratui:text4', {
            label: '|',
            isEnabled: () => false,
            execute: () => { }
        });
        app.commands.addCommand('ratui:equal', {
            label: '=',
            execute: () => insertText('=')
        });
        app.commands.addCommand('ratui:unequal', {
            label: '≠',
            caption: 'Alternativ: !=',
            execute: () => insertText('≠')
        });
        app.commands.addCommand('ratui:lt', {
            label: '<',
            execute: () => insertText('<')
        });
        app.commands.addCommand('ratui:lte', {
            label: '≤',
            caption: 'Alternativ: <=',
            execute: () => insertText('≤')
        });
        app.commands.addCommand('ratui:gte', {
            label: '≥',
            caption: 'Alternativ: >=',
            execute: () => insertText('≥')
        });
        app.commands.addCommand('ratui:gt', {
            label: '>',
            execute: () => insertText('>')
        });
    }
};
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.5de0ceaf740ac2b05c7b.js.map