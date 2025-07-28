"""
Implement a function that receives two IPv4 addresses, and returns the number of addresses between them 
(including the first one, excluding the last one).
All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

Examples
* With input "10.0.0.0", "10.0.0.50"  => return   50 
* With input "10.0.0.0", "10.0.1.0"   => return  256 
* With input "20.0.0.10", "20.0.1.0"  => return  246

"""
def ips_between(start, end):
    
    sumStart = 0
    sumEnd = 0
    start = start.split('.')
    end = end.split('.')
    
    sumStart =  int(start[0])* 256**3 + int(start[1])* 256**2 + int(start[2])* 256**1 + int(start[3]) 
        
    sumEnd =  int(end[0])* 256**3 + int(end[1])* 256**2 + int(end[2])* 256**1 + int(end[3]) 
    
    return (sumEnd - sumStart)
