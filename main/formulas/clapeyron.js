function clapeyron(constante = "mmHg", p = 0, v = 0, n = 0, r , t = 0) {
    var resultado;
  
    if (constante === "Pa") {
      r = 8.314;
    }
  
    if (constante === "atm") {
      r = 0.082;
    }
  
    if (constante === "mmHg") {
      r = 62.3;
    }
  
    if (constante === null) {}
  
    if (p === 0 && (v && n && t) !== 0) {
      resultado = n * r * t / v;
      return resultado;
    } else {
      if (v === 0 && (p && n && t) !== 0) {
        resultado = n * r * t / p;
        return resultado;
      } else {
        if (n === 0 && (p && v && t) !== 0) {
          resultado = p * v / (r * t);
          return resultado;
        } else {
          if (t === 0 && (p && v && n) !== 0) {
            resultado = p * v / (n * r);
            return resultado;
          } else {
            if (p && v && n && t !== 0) {
              return null;
            } else {
              if ((p && v && n && t) === 0) {
                return null;
              } else {}
            }
          }
        }
      }
    }
  }