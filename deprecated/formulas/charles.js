function charles(p1 = 0, p2 = 0, t1 = 0, t2 = 0) {
    var resultado;
  
    if (p1 === 0 && (p2 && t1 && t2) !== 0) {
      resultado = p2 * t1 / t2;
      return resultado;
    } else {
      if (p2 === 0 && (p1 && t1 && t2) !== 0) {
        resultado = p1 * t2 / t1;
        return resultado;
      } else {
        if (t1 === 0 && (p2 && p1 && t2) !== 0) {
          resultado = p1 * t2 / p2;
          return resultado;
        } else {
          if (t2 === 0 && (p2 && t1 && p1) !== 0) {
            resultado = p2 * t1 / p1;
            return resultado;
          } else {
            if (p1 && p2 && t1 && t2 !== 0) {
              return null;
            } else {
              if (p1 && p2 && t1 && t2 === 0) {
                return null;
              } else {}
            }
          }
        }
      }
    }
  }