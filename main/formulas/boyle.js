// (P1*V1) = (P2*V2)
// V = volume em litro
// P = Pressao em atm, mmHg ou Pa
// Eu nao tenho certeza de como esse codigo foi feito, favor nao mexer.

function boyle(p1 = 0, p2 = 0, v1 = 0, v2 = 0) {
    var resultado;
  
    if (v1 === 0 && (v2 && p1 && p2) !== 0) {
      resultado = v2 * p2 / p1;
      return resultado;
    } else {
      if (v2 === 0 && (v1 && p1 && p2) !== 0) {
        resultado = v1 * p1 / p2;
        return resultado;
      } else {
        if (p1 === 0 && (v2 && v1 && p2) !== 0) {
          resultado = v2 * p2 / p1;
          return resultado;
        } else {
          if (p2 === 0 && (v2 && p1 && v1) !== 0) {
            resultado = v1 * p1 / v2;
            return resultado;
          } else {
            if (v1 && v2 && p1 && p2 !== 0) {
              return null;
            } else {
              if ((v1 && v2 && p1 && p2) === 0) {
                return null;
              } else {}
            }
          }
        }
      }
    }
  }