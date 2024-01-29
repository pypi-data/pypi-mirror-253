import {
  AIConfigEditor,
  type AIConfigCallbacks,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";
import APITokenInput from "./APITokenInput";

type Props = {
  aiconfig: AIConfig;
  editorCallbacks: AIConfigCallbacks;
  onSetApiToken: (apiToken: string) => Promise<void>;
};

export default function GradioWorkbook(props: Props) {
  return (
    <div>
      <APITokenInput onSetToken={props.onSetApiToken} />
      <AIConfigEditor
        callbacks={props.editorCallbacks}
        aiconfig={props.aiconfig}
        mode="gradio"
      />
    </div>
  );
}
