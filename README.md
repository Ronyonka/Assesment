# Text Display

This is a python script that was developed to be used for pagination of text messages. Text messages are limited to 160 characters therefore once run the function is able to split the input text into chunks with 160 characters maximum


## Behaviour Driven Development

| Behaviour     | Input     | Output  |
| ------------- |:-------------:| -----:|
| Send a Text Message| The User inputs a Text Message | If the text is sent in 160 character chunks. |

As an example, the following message has 212 characters:

`As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30 pm. If you are unable to make this appointment, please call our customer service line at least 1 hour before your scheduled appointment time.`

The message should be sent in two chunks as such:

`As a reminder, you have an appointment with Dr. Smith tomorrow at 3:30 pm. If you are unable to make this appointment, please call our customer service  (1/2)`

and

`line at least 1 hour before your scheduled appointment time. (2/2)`


## Technologies Used

- Python3.6

## Setup/Installation Requirements


### Prerequisites
You need the following to run the project: -
* Python version 3
* git

### Clone this Repository

Clone this repository into your local machine to be able to run it and navigate into the folder


- `git clone https://github.com/Ronyonka/Assesment`

- `cd Assesment`


## Usage
Run the following command on the terminal/command line
```python
python3 text.py
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
