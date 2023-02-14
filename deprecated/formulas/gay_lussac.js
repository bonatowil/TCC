function gay_lussac(v1 = 0, v2 = 0, t1 = 0, t2 = 0) {
    var resultado;
  
    if (v1 === 0 && (v2 && t1 && t2) !== 0) {
      resultado = v2 * t1 / t2;
      return resultado;
    } else {
      if (v2 === 0 && (v1 && t1 && t2) !== 0) {
        resultado = v1 * t2 / t1;
        return resultado;
      } else {
        if (t1 === 0 && (v2 && v1 && t2) !== 0) {
          resultado = v1 * t2 / v2;
          return resultado;
        } else {
          if (t2 === 0 && (v2 && t1 && v1) !== 0) {
            resultado = v2 * t1 / v1;
            return resultado;
          } else {
            if (v1 && v2 && t1 && t2 !== 0) {
              return null;
            } else {
              if ((v1 && v2 && t1 && t2) === 0) {
                return null;
              } else {}
            }
          }
        }
      }
    }
  }