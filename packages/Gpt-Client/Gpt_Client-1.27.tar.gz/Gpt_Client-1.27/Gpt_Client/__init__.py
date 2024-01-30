# Thanks to the @xtekky. I was inspired by his project and created this one based on gpt4free

# Imports
from aiohttp import ClientSession

class Completion:
    '''
    Create chat completion with big text AI models for free
    '''
    @staticmethod
    async def create(
        model: str='gpt-4-0613',
        temperature: float=0.7,
        system_prompt: str='You are powerful AI assistant\n',
        messages: list=None
    ) -> str:
        '''
        Send question and get answer from model

        :param model: optional (default='gpt-4-0613'), the name of the AI model to use
        :type model: str
        :param temperature: optional (default=0.7), the temperature for generating responses
        :type temperature: float
        :param system_prompt: optional (default='You are powerful AI assistant'), the system prompt to use
        :type system_prompt: str
        :param messages: a list of messages for the chat. Example: [{"role": "system", "messages": "hello world"}]
        :type messages: list

        :returns: the generated answer from the model
        :returns type: str
        '''

        # check messages type
        if not isinstance(messages, list):
            raise RuntimeError(f'`Messages` must be a list, not {type(messages)}.\n'
                               'To fix, use await Completion.create(messages=[{"role": "user", "context": "hello, world!"}])')

        # create session
        async with ClientSession() as session:
            async with session.post(
                url='https://openchat.team/api/chat',
                json={
                    'model': {
                        'id': 'openchat_v3.2_mistral',
                        'name': model,
                    },
                    'messages': messages,
                    'prompt': system_prompt,
                    'temperature': temperature
                }
            ) as response:
                async for chunk in response.content.iter_any():
                    yield chunk.decode() # chunk in utf-8