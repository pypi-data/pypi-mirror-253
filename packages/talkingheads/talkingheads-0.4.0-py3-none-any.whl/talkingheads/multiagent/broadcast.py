'''Multiagent'''

import yaml
import asyncio
import model_library

client_map = {
    'ChatGPT' : model_library.ChatGPTClient,
    'HuggingChat' : model_library.HuggingChatClient,
    'Bard' : model_library.BardClient,
    'Pi' : model_library.PiClient
}

class TalkingHeads:
    """An interface for talking heads"""
    def __init__(self, configuration):
        with open(configuration) as fd:
            self.config = yaml.safe_load(fd)

        self.agent_list = []
        self.agent_map = {}

        for conf in enumerate(self.config.nodes):
            client = self.open_client(conf)
            self.agent_map[conf.tag] = client
            self.agent_list.append(client)

    def open_client(self, config):
        return 1

    def interact(self, question : str, head_number : int = None, head_name : str = None) -> str:
        """interact with the given head"""
        if head_number:
            client = self.agent_list[head_number]
        elif head_name:
            client = self.agent_map[head_name]
        else:
            raise NameError('Either head number or tag should be provided.')

        response = client.interact(question)
        return response

    async def broadcast(self, prompt):
        '''Sends message to all and returns back.'''
        responses = await asyncio.gather(
            *[
                asyncio.create_task(agent.interact(prompt))
                for agent in self.agent_map
            ]
        )
        return responses

    async def reset_all_threads(self):
        """reset heads for the given number"""
        reset_status = await asyncio.gather(
            *[
                asyncio.create_task(agent.reset_thread())
                for agent in self.agent_map
            ]
        )
        return all(reset_status)

    async def voting(self, prompt, voting_objective):
        """votes"""
        answers = await self.broadcast(prompt)
        voting_prompt = ' \n'.join([
            f'{idx})\n{answer}'
            for idx, answer in answers
        ])
        voting_prompt = f'''
        {voting_objective}
        Here are the options:
        {voting_prompt}
        Please provide your reasoning and at the end of your answer, provide your preference with the number indicator.
        '''
        selection = await self.broadcast(voting_prompt)
        best_option = [re.search('\d', i.split('\n')[-1]) for i in selection]
        best_option = 
        return all(reset_status)

