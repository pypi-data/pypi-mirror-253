<script lang="ts">
  //@ts-ignore Import IS used by react:GradioWorkbook below
  import GradioWorkbook from "./GradioWorkbook";
  import { client } from "@gradio/client";

  import "./styles.css";

  import type { Gradio } from "@gradio/utils";
  import { Block } from "@gradio/atoms";
  import { StatusTracker } from "@gradio/statustracker";
  import type { LoadingStatus } from "@gradio/statustracker";
  import type { SelectData } from "@gradio/utils";
  import {
    // AIConfigEditor,
    type RunPromptStreamCallback,
    type RunPromptStreamErrorCallback,
  } from "@lastmileai/aiconfig-editor";
  import type {
    AIConfig,
    InferenceSettings,
    JSONObject,
    Prompt,
  } from "aiconfig";

  type EventWithSessionIdData = {
    session_id: string;
  };

  type AddPromptEventData = EventWithSessionIdData & {
    prompt_name: string;
    prompt: Prompt;
    index: number;
  };

  // CancelRunEventData is used by the client to cancel a running threadID.
  // We don't directly interact with an AIConfig during this event so we
  // don't need to pass a session_id
  type CancelRunEventData = {
    cancellation_token_id: string;
  };

  type DeletePromptEventData = EventWithSessionIdData & {
    prompt_name: string;
  };

  type RunPromptEventData = EventWithSessionIdData & {
    prompt_name: string;
    cancellation_token?: string;
  };

  type SetConfigDescriptionEventData = EventWithSessionIdData & {
    description: string;
  };

  type SetConfigNameEventData = EventWithSessionIdData & {
    name: string;
  };

  type SetParametersEventData = EventWithSessionIdData & {
    parameters: JSONObject;
    prompt_name?: string;
  };

  type UpdateModelEventData = EventWithSessionIdData & {
    model_name?: string;
    model_settings?: InferenceSettings;
    prompt_name?: string;
  };

  type UpdatePromptEventData = EventWithSessionIdData & {
    prompt_name: string;
    prompt: Prompt;
  };

  export let elem_id = "";
  export let elem_classes: string[] = [];
  export let visible = true;

  // We obtain a serialized JSON string from the backend, containing
  // the aiconfig and model_ids
  export let value: string;
  let parsedValue: any;
  let aiconfig: AIConfig | undefined;
  let model_ids: string[] = [];

  // TODO: Can we just return the objects instead of serializing?
  type EventAPIResponse = {
    // Gradio client returns data as an array
    // (https://github.com/gradio-app/gradio/blob/main/client/js/src/client.ts#L40)
    // We return a JSON string on the server for the array value, so it results
    // in an array of strings
    data: string[];
  };

  // Root is provided to the component with the hostname. Rename below for clarity
  export let root: string;
  $: HOST_ENDPOINT = root;

  // Create a session id for every new client. We use this so that each client
  // has their own copy of an AIConfig so that when they make changes to it,
  // it doesn't overwrite the original AIConfig stored on the server
  const sessionId: string = Math.random().toString(36).substring(2);

  $: {
    try {
      if (value != null) {
        parsedValue = JSON.parse(value);
        const currentAIConfig: AIConfig | undefined =
          parsedValue.aiconfig ?? parsedValue.aiconfig_chunk;
        if (currentAIConfig) {
          aiconfig = currentAIConfig;
        }
        if (parsedValue.model_ids) {
          model_ids = parsedValue.model_ids;
        }
      }
    } catch (e) {
      console.error("Invalid JSON value passed to GradioWorkbook", e);
    }
  }

  export let container = true;
  export let scale: number | null = null;
  export let min_width: number | undefined = undefined;
  export let loading_status: LoadingStatus;
  export let gradio: Gradio<{
    change: never;
    select: SelectData;
    input: never;
    add_prompt: AddPromptEventData;
    cancel_run: CancelRunEventData;
    clear_outputs: EventWithSessionIdData;
    delete_prompt: DeletePromptEventData;
    remove_session_id: EventWithSessionIdData;
    run_prompt: RunPromptEventData;
    set_config_description: SetConfigDescriptionEventData;
    set_config_name: SetConfigNameEventData;
    set_parameters: SetParametersEventData;
    update_model: UpdateModelEventData;
    update_prompt: UpdatePromptEventData;
  }>;

  let gradioClient: any;
  async function getClient() {
    if (!gradioClient) {
      gradioClient = await client(`${HOST_ENDPOINT}`, {
        /*options*/
      });
    }
    return gradioClient;
  }

  async function handleAddPrompt(
    prompt_name: string,
    prompt: Prompt,
    index: number
  ) {
    const client = await getClient();
    const res = (await client.predict("/add_prompt_impl", undefined, {
      prompt_name,
      prompt,
      index,
      session_id: sessionId,
    })) as EventAPIResponse;

    return JSON.parse(res.data[0]);
  }

  async function handleCancel(cancellation_token_id: string) {
    const client = await getClient();
    await client.predict("/cancel_run_impl", undefined, {
      cancellation_token_id,
    });
  }

  async function handleClearOutputs() {
    const client = await getClient();
    const res = (await client.predict("/clear_outputs_impl", undefined, {
      session_id: sessionId,
    })) as EventAPIResponse;

    return JSON.parse(res.data[0]);
  }

  async function handleDeletePrompt(prompt_name: string) {
    const client = await getClient();
    await client.predict("/delete_prompt_impl", undefined, {
      prompt_name,
      session_id: sessionId,
    });
  }

  // TODO (rossdanlm): Implement this on the backend w. re.predicate
  function handleGetModels(search: string) {
    return model_ids.filter((model_id) =>
      model_id.toLowerCase().includes(search.toLowerCase())
    );
  }

  async function handleSetConfigDescription(description: string) {
    const client = await getClient();
    await client.predict("/set_config_description_impl", undefined, {
      description,
      session_id: sessionId,
    });
  }

  async function handleSetConfigName(name: string) {
    const client = await getClient();
    await client.predict("/set_config_name_impl", undefined, {
      name,
      session_id: sessionId,
    });
  }

  async function handleSetParameters(
    parameters: JSONObject,
    prompt_name?: string
  ) {
    const client = await getClient();
    await client.predict("/set_parameters_impl", undefined, {
      parameters,
      prompt_name,
      session_id: sessionId,
    });
  }

  // TODO: Refactor runPrompt callback to make stream/error callbacks optional
  async function handleRunPrompt(
    prompt_name: string,
    onStream: RunPromptStreamCallback,
    onError: RunPromptStreamErrorCallback,
    _enable_streaming?: boolean,
    cancellation_token?: string
  ) {
    const client = await getClient();
    // Use submit instead of predict to handle streaming from generator endpoint
    // See https://www.gradio.app/guides/getting-started-with-the-js-client#generator-endpoints
    const stream = await client.submit("/run_prompt_impl", undefined, {
      prompt_name,
      cancellation_token,
      session_id: sessionId,
    });

    stream.on("data", (dataEvent: EventAPIResponse) => {
      const event = JSON.parse(dataEvent.data[0] as string);

      const eventType = Object.keys(event)[0] as
        | "aiconfig_chunk"
        | "output_chunk"
        | "stop_streaming"
        | "error";

      if (eventType === "error") {
        onError({
          type: "error",
          data: {
            message: event.error.message ?? "Unknown error",
            code: event.error.code ? parseInt(event.error.code) : 500,
            data: event.error.data,
          },
        });
      } else {
        onStream({
          type: eventType,
          data: event[eventType],
        });
      }
    });
  }

  function handleUpdateModel(updateRequest: {
    modelName?: string;
    settings?: InferenceSettings;
    promptName?: string;
  }) {
    gradio.dispatch("update_model", {
      prompt_name: updateRequest.promptName,
      model_name: updateRequest.modelName,
      model_settings: updateRequest.settings,
      session_id: sessionId,
    });
  }

  async function handleUpdatePrompt(prompt_name: string, prompt: Prompt) {
    const client = await getClient();
    const res = (await client.predict("/update_prompt_impl", undefined, {
      prompt_name,
      prompt,
      session_id: sessionId,
    })) as EventAPIResponse;

    return JSON.parse(res.data[0]);
  }

  window.onpagehide = (event) => {
    if (!event.persisted && gradioClient) {
      gradioClient.predict("/remove_session_id_impl", undefined, {
        session_id: sessionId,
      });
    }
  };
</script>

<Block {visible} {elem_id} {elem_classes} {container} {scale} {min_width}>
  {#if loading_status}
    <StatusTracker
      autoscroll={gradio.autoscroll}
      i18n={gradio.i18n}
      {...loading_status}
    />
  {/if}
  <react:GradioWorkbook
    {aiconfig}
    callbacks={{
      addPrompt: handleAddPrompt,
      cancel: handleCancel,
      clearOutputs: handleClearOutputs,
      deletePrompt: handleDeletePrompt,
      getModels: handleGetModels,
      runPrompt: handleRunPrompt,
      setConfigDescription: handleSetConfigDescription,
      setConfigName: handleSetConfigName,
      setParameters: handleSetParameters,
      updateModel: handleUpdateModel,
      updatePrompt: handleUpdatePrompt,
    }}
  />
</Block>
