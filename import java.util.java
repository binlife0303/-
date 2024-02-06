import java.util.ArrayList;
import java.util.HashMap;

class FRP {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        int[] p = F(pattern);
        List<String> res = new ArrayList<String>();
        for (String w : words)
            if (Arrays.equals(F(w), p))
                res.add(w);
        return res;
    }

    public int[] F(String w) {
        HashMap<Character, Interger> m = new HashMap<>();
        int n = w.length();
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            m.putIfAbsent(w.charAt(i), m.size());
            res[i] = m.get(w.charAt(i));
        }
        return res;
    }

    public static void main(String[] args)
    {
        String[] words = {"abc", "deq", "mee", "aqq", "dkd", "ccc"};
        String pattern = "abb";
        FRP frp = new FRP();
        String[] results = frp.findAndReplacePattern(words, pattern);
        for(int i = 0;i < Array.length;i++)
            System.out.println(Array[i]);
    }
}