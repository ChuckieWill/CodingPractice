/*
* @Author: Yan_Daojiang
* @Date:   2019-05-17 09:57:02
* @Last Modified by:   13738
* @Last Modified time: 2019-05-17 09:57:13
*/
int missingNumber(int* nums, int numsSize){
    int s=0,f=0;
    for(int i=0;i<=numsSize;i++)
        s+=i;
    for(int i=0;i<numsSize;i++)
        f+=nums[i];
    return s-f;
}