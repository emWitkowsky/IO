// Reguły drzewa decyzyjnego

if (feature[10] <= -1.75) {
  if (feature[12] <= -1.66) {
    return 'class [0. 0. 0. ... 0. 0. 0.]';
  } else {  // if (feature[12] > -1.66)
    return 'class [0. 0. 0. ... 0. 0. 0.]';
  }
} else {  // if (feature[10] > -1.75)
  if (feature[10] <= -1.74) {
    if (feature[0] <= -1.95) {
      return 'class [0. 0. 0. ... 0. 0. 0.]';
    } else {  // if (feature[0] > -1.95)
      if (feature[1] <= 1.18) {
        return 'class [0. 0. 0. ... 0. 0. 0.]';
      } else {  // if (feature[1] > 1.18)
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
