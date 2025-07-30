import java.util.*;

public class Main {
    static int N, M;
    static int[][] grid;
    static int[][] dist;
    // 8방향 (상하좌우+대각선)
    static int[] dx = {-1, -1, -1, 0, 1, 1, 1, 0};
    static int[] dy = {-1, 0, 1, 1, 1, 0, -1, -1};

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        grid = new int[N][M];
        dist = new int[N][M];

        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                grid[i][j] = sc.nextInt();
                dist[i][j] = -1; // 거리 초기화
                if (grid[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                    dist[i][j] = 0; // 아기 상어 위치는 거리 0
                }
            }
        }

        // 다중 출발 BFS
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0];
            int y = curr[1];

            for (int d = 0; d < 8; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx >= 0 && ny >= 0 && nx < N && ny < M) {
                    if (dist[nx][ny] == -1) { // 방문하지 않은 칸이면
                        dist[nx][ny] = dist[x][y] + 1;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
        }

        // 안전 거리 최대값 계산
        int maxDist = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == 0) { // 빈 칸 중
                    maxDist = Math.max(maxDist, dist[i][j]);
                }
            }
        }

        System.out.println(maxDist);
        sc.close();
    }
}
