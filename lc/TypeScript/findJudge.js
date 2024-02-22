var findJudge = function (N, trust) {
  var trustCount = new Array(N + 1).fill(0);
  for (var _i = 0, trust_1 = trust; _i < trust_1.length; _i++) {
    var _a = trust_1[_i],
      a = _a[0],
      b = _a[1];
    trustCount[a]--;
    trustCount[b]++;
  }
  for (var i = 1; i <= N; i++) {
    if (trustCount[i] === N - 1) return i;
  }
  return -1;
};

console.log(findJudge(2, [[1, 2]]));
