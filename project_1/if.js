// Reguły drzewa decyzyjnego

if (feature[10] <= -1.75) {
  if (feature[10] <= -1.83) {
    return 'class [0. 0. 0. ... 0. 0. 0.]';
  } else {  // if (feature[10] > -1.83)
    return 'class [0. 0. 0. ... 0. 0. 0.]';
  }
} else {  // if (feature[10] > -1.75)
  if (feature[10] <= -1.74) {
    if (feature[11] <= 0.40) {
      return 'class [0. 0. 0. ... 0. 0. 0.]';
    } else {  // if (feature[11] > 0.40)
      if (feature[11] <= 1.02) {
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      } else {  // if (feature[11] > 1.02)
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      }
    }
  } else {  // if (feature[10] > -1.74)
    if (feature[9] <= 2.12) {
      if (feature[1] <= 1.35) {
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      } else {  // if (feature[1] > 1.35)
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      }
    } else {  // if (feature[9] > 2.12)
      if (feature[9] <= 2.12) {
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      } else {  // if (feature[9] > 2.12)
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      }
    }
  }
}
