import { expect, test } from '@jupyterlab/galata';

/**
 * Don't load JupyterLab webpage before running the tests.
 * This is required to ensure we capture all log messages.
 */
test.use({ autoGoto: false });

test.describe('PDF Export command', () => {
  test('should not appear on palette at Launcher', async ({ page }) => {
    await page.goto();

    await page.getByText('View', { exact: true }).click();
    await page.getByText('Activate Command Palette').click();
    await page.getByPlaceholder('SEARCH', { exact: true }).fill('satysfi');

    await expect(page.getByText('No commands found')).toContainText(
      "No commands found that match 'satysfi'"
    );
  });
});
