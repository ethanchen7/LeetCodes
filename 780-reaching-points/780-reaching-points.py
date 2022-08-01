class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:   
        
        while tx >= sx and ty >= sy:
            
            if tx == sx and ty == sy:
                return True
                
            if tx == sx:
                if (ty - sy) % tx == 0:
                    return True
                else:
                    return False
                
            elif ty == sy:
                if (tx - sx) % ty == 0:
                    return True
                else:
                    return False
        
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
                
                
        return False