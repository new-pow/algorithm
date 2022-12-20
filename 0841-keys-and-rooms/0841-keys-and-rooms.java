class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] opens = new boolean[rooms.size()];
        Stack<Integer> keys = new Stack<>();

        opens[0] = true;

        for (int i=0; i<rooms.get(0).size(); i++) {
            keys.push(rooms.get(0).get(i));
        }

        while (keys.size()!=0) {
            int key = keys.pop();
            if (!opens[key]) {
                opens[key] = true;
                for (int i=0; i<rooms.get(key).size(); i++) {
                    keys.push(rooms.get(key).get(i));
                }
            }
        }

        for (int i=0; i<rooms.size(); i++) {
            if (!opens[i]) return false;
        }
        return true;
    }
}