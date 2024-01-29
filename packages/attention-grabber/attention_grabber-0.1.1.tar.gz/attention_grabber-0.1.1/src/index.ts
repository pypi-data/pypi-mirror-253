import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';

import { NotebookActions, INotebookTracker } from '@jupyterlab/notebook';

/**
 * Initialization data for the attention-grabber extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'attention-grabber:plugin',
  description:
    'Flashes your screen when cells are finished, until you click on the notebook again.',
  autoStart: true,
  requires: [INotebookTracker],
  activate: (app: JupyterFrontEnd, notebookTracker: INotebookTracker) => {
    console.log('JupyterLab extension attention-grabber is activated!');

    const audioContext = new AudioContext();
    let annoyingInterval: number | null = null;
    let grabAttentionTimeout: number | null = null;
    let isPlaying = false;
    let oscillator: OscillatorNode | null = null;
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
        oscillator.frequency.setValueAtTime(1000, audioContext.currentTime);
        oscillator.connect(audioContext.destination);
        oscillator.start();

        // Change screen color
        document.body.style.backgroundColor = 'red';
      } else {
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

    NotebookActions.executed.connect(() => {
      if (extensionEnabled) {
        if (grabAttentionTimeout !== null) {
          clearTimeout(grabAttentionTimeout);
        }
        grabAttentionTimeout = setTimeout(
          grabAttention,
          3000
        ) as unknown as number; // Start effect 3 seconds after execution
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

export default plugin;
