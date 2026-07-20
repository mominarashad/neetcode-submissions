class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        let start=0;
        let max_len=1;
        let n=s.length;
        for(let i=0; i<n; i++){
            let low=i;
            let high=i;

            while (low>=0 && high<n && s[low]==s[high]){
                let curr_len=high-low+1;

                if (curr_len>max_len){
                    start=low;
                    max_len=curr_len;

                }
                low-=1;
                high+=1;
            }

            low=i;
            high=i+1;

            while (low>=0 && high<n && s[low]==s[high]){
                let curr_len=high-low+1;

                if (curr_len>max_len){
                    start=low;
                    max_len=curr_len;

                }
                low-=1;
                high+=1;
            }

        
        }
        return s.substring(start,start+ max_len);
    
    }
}
