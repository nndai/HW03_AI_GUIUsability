// Survey environment only: preserve SUT logic, substitute API port 3000 -> 13000.
import react from '../../eshop-sut/frontend-web/node_modules/@vitejs/plugin-react/dist/index.js';
import { fileURLToPath } from 'node:url';

export default {
  root: fileURLToPath(new URL('../../eshop-sut/frontend-web/', import.meta.url)),
  plugins: [
    {
      name: 'survey-api-port',
      enforce: 'pre',
      transform(code, id) {
        if (/\.[jt]sx?$/.test(id) && !id.includes('node_modules')) {
          return code.replaceAll('http://localhost:3000', 'http://localhost:13000');
        }
      },
    },
    react(),
  ],
  server: { host: '127.0.0.1', port: 5175, strictPort: true },
};
