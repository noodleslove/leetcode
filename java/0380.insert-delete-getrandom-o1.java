// Created by Eddie Ho at 2023/11/19 11:31
// leetgo: 1.3.8
// https://leetcode.com/problems/insert-delete-getrandom-o1/

// @lc code=begin

import java.util.*;

class RandomizedSet {

    private List<Integer> _array;
    private Map<Integer, Integer> _map;

    public RandomizedSet() {
        this._array = new ArrayList<>();
        this._map = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (_map.containsKey(val)) { return false; }
        int index = _array.size();
        _map.put(val, index);
        return _array.add(val);
    }
    
    public boolean remove(int val) {
        int index = _map.getOrDefault(val, -1);
        if (index == -1) { return false; }
        if (index < _array.size() - 1) {
            int lastOne = _array.get(_array.size() - 1);
            _array.set(index, lastOne);
            _map.put(lastOne, index);
        }
        _map.remove(val);
        _array.remove(_array.size() - 1);
        return true;
    }
    
    public int getRandom() {
        Random rand = new Random();
        return _array.get(rand.nextInt(_array.size()));
    }
}

// @lc code=end
