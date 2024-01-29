import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { ICommandPalette, MainAreaWidget } from '@jupyterlab/apputils';
import { NotebookPanel } from '@jupyterlab/notebook';
import { IRenderMimeRegistry, MimeModel } from '@jupyterlab/rendermime';
import { KernelMessage } from '@jupyterlab/services';
import { CMD_EXPORT_PDF } from './consts';

/**
 * Initialization data for the satysfi-notebook-tweaks extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'satysfi-notebook-tweaks:plugin',
  description: 'A small tweaks for SATySFi Notebook environment.',
  autoStart: true,
  requires: [ICommandPalette, IRenderMimeRegistry],
  activate: (
    app: JupyterFrontEnd,
    palette: ICommandPalette,
    rendermime: IRenderMimeRegistry
  ) => {
    app.commands.addCommand(CMD_EXPORT_PDF, {
      label: 'SATySFi Notebook: Export entire document as PDF',
      isVisible: () => {
        const widget = app.shell.currentWidget;
        return (
          widget instanceof NotebookPanel &&
          widget.sessionContext.kernelPreference.language?.toLowerCase() ===
            'satysfi'
        );
      },
      execute: async () => {
        const nb = app.shell.currentWidget;
        if (!(nb instanceof NotebookPanel) || !nb.model) {
          return;
        }
        const workingKernel = nb.sessionContext.session?.kernel;
        if (!workingKernel) {
          return;
        }

        const cells = nb.model.sharedModel.cells.filter(
          ({ cell_type }) => cell_type === 'code'
        );
        const mods = cells
          .filter(({ source }) => source.startsWith('%!'))
          .map(({ source }) => source.slice(2));
        const document = cells
          .filter(
            ({ source }) =>
              !source.startsWith('%!') &&
              !source.startsWith('%?') &&
              !source.startsWith('%%')
          )
          .map(({ source }) => source)
          .join('\n');

        const renderingKernel = await app.serviceManager.kernels.startNew(
          {
            name: workingKernel.name
          },
          {
            clientId: workingKernel.clientId,
            username: workingKernel.username,
            handleComms: workingKernel.handleComms
          }
        );
        renderingKernel.requestExecute({ code: '%% render-in-pdf' });
        mods.forEach(mod => renderingKernel.requestExecute({ code: mod }));
        const future = renderingKernel.requestExecute({ code: document });
        future.onIOPub = msg => {
          if (!KernelMessage.isExecuteResultMsg(msg)) {
            return;
          }

          renderingKernel.shutdown();
          const pdf = rendermime.createRenderer('application/pdf');
          const tab = new MainAreaWidget({
            content: pdf
          });
          tab.title.label = `PDF Export: ${nb.title.label}`;
          tab.id = `${nb.id}-exported-pdf`;
          tab.revealed.then(() => {
            pdf.renderModel(new MimeModel(msg.content));
          });
          app.shell.add(tab, 'main', { mode: 'tab-after' });
        };
      }
    });

    palette.addItem({
      command: CMD_EXPORT_PDF,
      category: 'notebook'
    });
  }
};

export default plugin;
