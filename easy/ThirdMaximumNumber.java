public class Solution
{
    public int thirdMax(int[] nums)
    {
        long first, second, third;
        first = second = third = Long.MIN_VALUE;
        for (int num : nums)
        {
            if (num == first || num == second || num == third) continue;
            if (num > first)
            {
                third = second;
                second = first;
                first = num;
            }
            else if (num > second)
            {
                third = second;
                second = num;
            }
            else if (num > third) third = num;
        }

        return (third == Long.MIN_VALUE) ? (int)first : (int)third;
    }
}

        