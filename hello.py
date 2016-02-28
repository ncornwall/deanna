from flask import Flask
from flask import render_template
from flask import request
from flask_oauth import OAuth
from flask import session

oauth = OAuth()
the_remote_app = oauth.remote_app('slack',
    base_url='https://slack.com/',
    request_token_url='https://slack.com/api/oauth.access',
    access_token_url='https://slack.com/api/oauth.access',
    authorize_url='https://slack.com/api/oauth.access',
    consumer_key='3927713261.23411567264',
    consumer_secret='7eff0ae701eb73a07cab2b5c9d091795'
)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/auth', methods=['GET', 'POST'])
def auth():
        post_data['text'] = text
        post_url = "http://slack.oauth.access" 
        results = self.s.post(url=post_url, data=post_data)
        return results.text

@slack.tokengetter
def get_slack_token(token=None):
	print session.get('slack_token')
    return session.get('slack_token')

if __name__ == '__main__':
    app.run()