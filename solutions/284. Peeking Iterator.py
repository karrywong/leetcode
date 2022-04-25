        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self._peeked_value is None:
            if not self._iterator.hasNext():
                raise StopIteration()
            self._peeked_value = self._iterator.next()
​
        return self._peeked_value
​
    def next(self):
        """
        :rtype: int
        """
        if self._peeked_value is not None:
            to_return = self._peeked_value
            self._peeked_value = None
            return to_return
​
        if not self._iterator.hasNext():
            raise StopIteration()
​
        # Otherwise, we need to return a new value.
        return self._iterator.next()
    def hasNext(self):
        """
        :rtype: bool
        """
        return self._peeked_value is not None or self._iterator.hasNext()
​
# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
