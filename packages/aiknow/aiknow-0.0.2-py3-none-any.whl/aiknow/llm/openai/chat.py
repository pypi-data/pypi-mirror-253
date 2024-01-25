from openai import OpenAI, AsyncOpenAI

from .auth import OpenAIAuth
from ..chat import (
    ChatModel,
    ChatMessage,
    UserChatMessage,
    ChatResponse,
    ChatTokenUsage,
)
from .response import OpenAIStreamedChatResponse, AsyncOpenAIStreamedChatResponse


class OpenAIChatModel(ChatModel):
    auth: OpenAIAuth = OpenAIAuth()

    def get_complete_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Convert a single message to a list
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        response = OpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response.choices[0].message.content,
            token_usage=ChatTokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            ),
        )

        return response

    def get_streamed_response(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> OpenAIStreamedChatResponse:
        # Convert a single message to a list
        messages = self._convert_to_chat_message_list(messages)

        # Call the API and get the stream
        stream = OpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Create a streamed response
        streamed_response = OpenAIStreamedChatResponse(stream)

        return streamed_response

    async def get_complete_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> ChatResponse:
        # Convert a single message to a list
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        response = await AsyncOpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
        )

        # Convert a ChatResponse
        response = ChatResponse(
            content=response.choices[0].message.content,
            token_usage=ChatTokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            ),
        )

        return response

    async def get_streamed_response_async(
        self,
        messages: str | UserChatMessage | list[ChatMessage],
    ) -> AsyncOpenAIStreamedChatResponse:
        # Convert a single message to a list
        messages = self._convert_to_chat_message_list(messages)

        # Call the API
        stream = await AsyncOpenAI(api_key=self.auth.api_key).chat.completions.create(
            model=self.name,
            messages=list(
                map(
                    lambda message: dict(
                        role=message.role.value,
                        content=message.content,
                    ),
                    messages,
                )
            ),
            temperature=self.temperature,
            # Enable streaming
            stream=True,
        )

        # Create a streamed response
        streamed_response = AsyncOpenAIStreamedChatResponse(stream)

        return streamed_response
