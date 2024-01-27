```
# lazy_serve

A simple, easy-to-use Python package for starting HTTP servers with minimal setup. Ideal for serving static files in development environments or for lightweight file sharing.

## Installation

To install lazy_serve, simply use pip:

```bash
pip install lazy_serve
```


## Usage

Using lazy_serve is straightforward. Here's a basic example:

```python
import lazy_serve as lz

if __name__ == "__main__":
    servers = [(8080, "~/server1/out/"), (8081, "~/server2/out/")]
    lz.serve(servers)
```

This code will start HTTP servers on ports 8080 and 8081, serving files from `~/server1/out/` and `~/server2/out/` respectively.

## Features

- **Easy to Use:** Start a server in just a few lines of code.
- **Flexible:** Serve any directory by simply specifying its path.
- **Concurrent Servers:** Run multiple servers at once, each on its own port.

## Requirements

- Python 3.6 or higher

## Contributing

Contributions to lazy_serve are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature.
3. Add your feature or bug fix.
4. Run the tests to ensure everything is working.
5. Submit a pull request.

## License

This project is licensed under the MIT License.
