const findJudge = (N: number, trust: number[][]) => {
  const trustCount = new Array(N + 1).fill(0);
  for (const [a, b] of trust) {
    trustCount[a]--;
    trustCount[b]++;
  }
  for (let i = 1; i <= N; i++) {
    if (trustCount[i] === N - 1) return i;
  }
  return -1;
};

findJudge(2, [[1, 2]]);
