class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int n = nums.length;
        int arr[] = new int[n];
        int count=0;
        for(int i=0;i<n;i++){
            if(nums[i]%2==0){
                arr[count++]=nums[i];
            }
        }
        for(int i=0;i<n;i++){
            if(nums[i]%2 !=0){
                arr[count++]=nums[i];
            }
        }
        
     
       return arr; 
    }
}