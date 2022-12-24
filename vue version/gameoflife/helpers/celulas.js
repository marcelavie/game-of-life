/**
 *
 *
 * @param {number} valor
 * @param {number} min
 * @param {number} max
 */
export const Intervalo = (valor, min, max) => {
    return !(valor < min || valor > max)
  }
  