import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static Node root = new Node('A',null,null);

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i=0; i<n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char data = st.nextToken().charAt(0);
            char left = st.nextToken().charAt(0);
            char right = st.nextToken().charAt(0);
            Node temp = new Node();
            temp.insertNode(root, data, left, right);
        }
        
        Order order = new Order();
        
        order.preorder(root);
        System.out.println();
        order.inorder(root);
        System.out.println();
        order.postorder(root);
    }
}

class Node {
    char value;
    Node left;
    Node right;
    
    public Node(){}

    public Node(char value, Node left, Node right) {
        this.value = value;
        this.left = left;
        this.right = right;
    }

    public static void insertNode(Node temp, char root, char left, char right) {


        if (temp.value == root) {
            temp.left = (left == '.' ? null : new Node(left,null,null));
            temp.right = (right == '.' ? null : new Node(right,null,null));
        }
        else {
            if(temp.left != null) insertNode(temp.left, root, left, right);
            if(temp.right != null) insertNode(temp.right, root, left, right);
        }
    }
}

class Order {
    public Order(){}
    public static void preorder(Node node){
        if(node!=null) {
            System.out.print(node.value);
            preorder(node.left);
            preorder(node.right);
        }
    }

    public static void inorder(Node node){
        if(node!=null) {
            inorder(node.left);
            System.out.print(node.value);
            inorder(node.right);
        }
    }

    public static void postorder(Node node){
        if(node!=null) {
            postorder(node.left);
            postorder(node.right);
            System.out.print(node.value);
        }
    }
}