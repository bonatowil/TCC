function density(d = 0, m = 0, v = 0) {
    var resultado;
  
    if (v === 0 && (d && m) !== 0) {
      resultado = m / d;
      return [d, m, resultado];
    } else {
      if (m === 0 && (v && d) !== 0) {
        resultado = d * v;
        return [d, resultado, v];
      } else {
        if (d === 0 && (v && m) !== 0) {
          resultado = m / v;
          return [resultado, m, v];
        } else {
          if (d && m && v !== 0) {
            return [d, m, v];
          } else {
            if ((d && v && m) === 0) {
              return [d, m, v];
            } else {
              return [d, m, v];
            }
          }
        }
      }
    }
  }