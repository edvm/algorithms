# Infinite Monkey Theorem

The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare.

![Monkey typing](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3c/Chimpanzee_seated_at_typewriter.jpg/220px-Chimpanzee_seated_at_typewriter.jpg)

Here goes my implementation! (Use Python >= 3.8)

## Usage

```python
In [1]: import monkey

In [2]: monkey.start_typing('python', repeat=1000)
Original phrase is: python
Monkey generated this one: yjxhwn
Score: 33.33%
Iterations: 1000
Used 100.00% of given iterations
Time elapsed: 0.010 seconds
```

OR make your monkey more smart using an optimization of the above algorithm. Just pass `use_opt1` argument like: 

```python
In [3]: monkey.start_typing('python', repeat=1000, use_opt1=True)
Original phrase is: python
Monkey generated this one: python
Score: 100.00%
Iterations: 48
Used 4.80% of given iterations
Time elapsed: 0.000 seconds
```

OR just call generate

```python
>>> import monkey
>>> monkey.generate('python', repeat=10000)
('ykthon', 4, 15082)
```

OR just call a smarter generate

```python
>>> monkey.generate('python', repeat=1000, use_opt1=True)
>>> ('python', 6, 899)
```
