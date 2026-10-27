
class MyHashSet:

    def __init__(self, capacity=789):
        self.capacity=capacity
        self.buckets=[[]for _ in range(capacity)]

    def _hash(self,key):
        return key % self.capacity    

    def add(self, key: int) -> None:
        index=self._hash(key)
        bucket=self.buckets[index]

        if key not in bucket:
            bucket.append(key)
       

    def remove(self, key: int) -> None:
        index=self._hash(key)
        bucket=self.buckets[index]

        for i in range(len(bucket)):
            if key == bucket[i]:
                bucket.pop(i)
                return
        

    def contains(self, key: int) -> bool:
        index=self._hash(key)
        bucket=self.buckets[index]
        for item in bucket:
            if item == key:
                return True
        return False        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)