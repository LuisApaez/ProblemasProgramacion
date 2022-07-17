// Solucion problema 2

public class problema2 {
    public static void main(String[] args) {
        int[] intArray = new int[]{2,7,11,15};
        int target = 22;
        System.out.println(-10 * (3 + 4) / 2);
        System.out.println(twoSums(intArray, target)[0]+" "+twoSums(intArray, target)[1]); 
    }

    // Metodo solucion
    public static int[] twoSums(int[] nums, int target) {
        int[] res = new int[2];
    
        for(int i=0;i<nums.length;i++){
            for(int j=i+1;j<nums.length;j++){
                if(nums[i] + nums[j] == target){
                    res[0]=i;
                    res[1]=j;
                    break;
                }
            }
        }
        return res;
    }
}
