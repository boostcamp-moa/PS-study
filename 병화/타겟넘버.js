function solution(numbers, target) {
    let answer = 0;

    dfs(0, 0);

    function dfs(index, sum) {
        // 배열의 마지막 index에 도달했을 때 target 값과 일치하는지 확인
        if (index === numbers.length) {
            if (sum === target) {
                answer++;
            }
            return;
        }

        // 배열의 index번째 값이 더해지는 경우
        dfs(index + 1, sum + numbers[index]);
        // 배열의 index번째 값이 빼지는 경우
        dfs(index + 1, sum - numbers[index]);
    }
    return answer;
}
