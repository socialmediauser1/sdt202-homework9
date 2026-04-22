public class Driver {

    public static void main(String[] args) {
        OrderedSymbolTable<String, Integer> st = new BST<>();

        System.out.println("== Empty table ==");
        System.out.println("isEmpty() = " + st.isEmpty());
        System.out.println("size()    = " + st.size());

        System.out.println();
        System.out.println("== Inserting S E A R C H E X A M P L E ==");
        String input = "S E A R C H E X A M P L E";
        String[] tokens = input.split(" ");
        for (int i = 0; i < tokens.length; i++) {
            st.put(tokens[i], i);
            System.out.println("put(\"" + tokens[i] + "\", " + i + ")");
        }

        System.out.println();
        System.out.println("== Basic queries ==");
        System.out.println("size()          = " + st.size());
        System.out.println("isEmpty()       = " + st.isEmpty());
        System.out.println("contains(\"E\")   = " + st.contains("E"));
        System.out.println("contains(\"Z\")   = " + st.contains("Z"));
        System.out.println("get(\"R\")        = " + st.get("R"));
        System.out.println("get(\"Z\")        = " + st.get("Z"));

        System.out.println();
        System.out.println("== Ordered queries ==");
        System.out.println("min()           = " + st.min());
        System.out.println("max()           = " + st.max());
        System.out.println("floor(\"G\")      = " + st.floor("G"));
        System.out.println("ceiling(\"G\")    = " + st.ceiling("G"));
        System.out.println("rank(\"M\")       = " + st.rank("M"));
        System.out.println("select(3)       = " + st.select(3));

        System.out.println();
        System.out.println("== Range queries ==");
        System.out.println("size(\"C\",\"M\")   = " + st.size("C", "M"));
        System.out.print("keys(\"C\",\"M\")   = [");
        boolean first = true;
        for (String k : st.keys("C", "M")) {
            if (!first) System.out.print(", ");
            System.out.print(k);
            first = false;
        }
        System.out.println("]");

        System.out.println();
        System.out.println("== Full iteration ==");
        System.out.print("keys()          = [");
        first = true;
        for (String k : st.keys()) {
            if (!first) System.out.print(", ");
            System.out.print(k);
            first = false;
        }
        System.out.println("]");

        System.out.println();
        System.out.println("== Deletions ==");
        st.deleteMin();
        System.out.println("after deleteMin()   size = " + st.size() + ", keys = " + toList(st.keys()));
        st.deleteMax();
        System.out.println("after deleteMax()   size = " + st.size() + ", keys = " + toList(st.keys()));
        st.delete("E");
        System.out.println("after delete(\"E\")   size = " + st.size() + ", keys = " + toList(st.keys()));

        System.out.println();
        System.out.println("== put(key, null) removes key ==");
        st.put("X", 99);
        System.out.println("before: contains(\"X\") = " + st.contains("X") + ", size = " + st.size());
        st.put("X", null);
        System.out.println("after put(\"X\", null): contains(\"X\") = " + st.contains("X") + ", size = " + st.size());
        System.out.println("final keys = " + toList(st.keys()));
    }

    private static String toList(Iterable<String> it) {
        StringBuilder sb = new StringBuilder("[");
        boolean first = true;
        for (String k : it) {
            if (!first) sb.append(", ");
            sb.append(k);
            first = false;
        }
        sb.append("]");
        return sb.toString();
    }
}
