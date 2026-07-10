class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        finish=0
        final=float('inf')
        result=0
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                finish=landStartTime[i]+landDuration[i]
    
                result=max(finish,waterStartTime[j]) + waterDuration[j]
                final=min(result,final)

        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                finish=waterDuration[i]+waterStartTime[i]
                result=max(finish,landStartTime[j])+landDuration[j]
                final=min(result,final)

        return final

            
            