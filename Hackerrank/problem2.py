# Store 1st element of
        # sub-array into set
        s.add(arr[i])
 
        for j in range(i + 1, n):
             
            # Check absolute difference
            # between two elements
            if (abs(arr[i] - arr[j]) == 0 or
                abs(arr[i] - arr[j]) == k):
 
                # If the new element is not
                # present in the set
                if (not arr[j] in s):
 
                    # If the set contains
                    # two elements
                    if (len(s) == 2):
                        break
 
                    # Otherwise
                    else:
                        s.add(arr[j])
                         
            else:
                break
 
        if (len(s) == 2):
 
            # Update the maximum length
            Max = max(Max, j - i)
 
            # Remove the set elements
            s.clear()
 
        else:
            s.clear()
 