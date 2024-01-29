import {
  AIConfigEditor,
  type AIConfigCallbacks,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";

type Props = {
  aiconfig: AIConfig;
  callbacks: AIConfigCallbacks;
};

export default function GradioWorkbook(props: Props) {
  return (
    <AIConfigEditor
      callbacks={props.callbacks}
      aiconfig={props.aiconfig}
      mode="gradio"
    />
  );
}
