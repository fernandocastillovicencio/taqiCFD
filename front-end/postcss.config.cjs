// filepath: c:\Users\enzol\OneDrive\Área de Trabalho\taqiCFD\frontend\postcss.config.cjs
const isProduction = process.env.NODE_ENV === 'production'

module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
    ...(isProduction && {
      cssnano: {
        preset: ['default', {
          discardComments: { removeAll: true },
          normalizeWhitespace: true,
        }],
      },
    }),
  },
}
