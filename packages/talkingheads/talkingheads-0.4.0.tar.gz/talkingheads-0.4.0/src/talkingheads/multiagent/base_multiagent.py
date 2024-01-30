"""Multiagent"""

import asyncio
import logging

import yaml
from talkingheads import model_library

client_map = {
    "ChatGPT": model_library.ChatGPTClient,
    "HuggingChat": model_library.HuggingChatClient,
    "Bard": model_library.BardClient,
    "Pi": model_library.PiClient,
}


class TalkingHeads:
    """An interface for talking heads"""

    def __init__(self, configuration):
        with open(configuration) as fd:
            self.config = yaml.safe_load(fd)

        self.agent_list = []
        self.agent_map = {}
        self.master_head = None

        for conf in enumerate(self.config.nodes):
            client = self.open_client(conf)
            self.agent_map[conf.tag] = client
            self.agent_list.append(client)

    def open_client(self, config):
        return 1

    def set_master_head(self, head_number: int = None, head_name: str = None) -> bool:
        if not head_name or head_number:
            logging.error("Either provide head_number or head_name")
            return False

        head = self.agent_map.get(head_name)
        if not head:
            logging.error("No such head %s exists.", head_name)
            return False
        self.master_head = head
        return True

    def interact(
        self, question: str, head_number: int = None, head_name: str = None
    ) -> str:
        """interact with the given head"""
        if head_number:
            client = self.agent_list[head_number]
        elif head_name:
            client = self.agent_map[head_name]
        else:
            raise NameError("Either head number or tag should be provided.")

        response = client.interact(question)
        return response

    async def broadcast(self, prompt, exclude_master=False):
        """Sends message to all and returns back."""
        heads = list(self.agent_map.values())
        if exclude_master:
            heads.remove(self.master_head)

        responses = await asyncio.gather(
            *[asyncio.create_task(agent.interact(prompt)) for agent in heads]
        )
        return responses

    async def reset_all_threads(self):
        """reset heads for the given number"""
        reset_status = await asyncio.gather(
            *[asyncio.create_task(agent.reset_thread()) for agent in self.agent_map]
        )
        return all(reset_status)

    async def aggregate(self, prompt: str, agg_objective: str):
        """This function collects a number of responses and aggregates them.
        The aggregation can differ in logical means. Some examples:
        - Compose a new message
        - Select the best message
        - Select the worst message
        - Find the most reoccuring number
        - Check if all the answers are the semantically similar

        Not all chat models can read lengthy inputs, remind your chat models to keep it short!

        Args:
            prompt (str): The prompt to pass on model swarm.
            agg_objective (str): The prompt to pass on master head to apply the aggregation.

        Returns:
            (str): The response of the master head.
        """
        if self.master_head is None:
            raise RuntimeError("Set master head before voting operation")

        answers = await self.broadcast(prompt, exclude_master=True)
        answers = " \n".join(
            [f"{idx})\n{answer}" for idx, answer in enumerate(answers)]
        )
        final_prompt = f"""
        {agg_objective}
        Here are the options:
        {answers}
        """
        final_answer = self.master_head(final_prompt)
        return final_answer
