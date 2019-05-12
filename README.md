# SERC

SERC, is Super Easy Rest Client. It is an interactive console app that I do to make your http requests via the command line easily.

## Installation

Use the git clone to install SERC.

```bash
git clone git@github.com:serkanerip/SERC.git
```

## Usage

```bash
cd serc
python3 main.py
```

## Commands

- base : For setting a base url for your requests.
- get, post, patch, delete : For making http requests.
- = : Creating variables to use after in commands.(as soon as)
- resp : Getting response of your last request.
- addh : Adding new header to your request.
- delh : Delete a header in your headers.
- showh: Show your headers.
- last: The last process is repeated.

## Examples

```bash
[SERC]: base http://localhost:3000
[SERC]: get, $base
<Response [404]>
[SERC]: resp
[Headers]: { 'Content-Type': 'application/json' }
[Json]:  {'status': 404, 'success': 'false', 'message': 'Method Not Found!'}
[SERC]: showh
{'Accept': 'application/json'}
[SERC]: addh Content-Type application/json
[SERC]: post, $base/api/user/signup, { "email":"serkanerip@gmail.com", "password":"123456"}
<Response [201]>
[SERC]: q
Thank you for using SERC.
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
