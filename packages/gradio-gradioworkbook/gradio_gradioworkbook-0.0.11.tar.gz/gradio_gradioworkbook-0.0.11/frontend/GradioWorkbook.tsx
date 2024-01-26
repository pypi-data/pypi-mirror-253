import {
  AIConfigEditor,
  type AIConfigCallbacks,
} from "@lastmileai/aiconfig-editor";
import type { AIConfig } from "aiconfig";
import { MantineProvider } from "@mantine/core";
import { Notifications, showNotification } from "@mantine/notifications";

type Props = {
  aiconfig: AIConfig;
  callbacks: AIConfigCallbacks;
};

function Test() {
  showNotification({
    title: "Test notification",
    message: "test",
    color: "red",
    autoClose: false,
  });
  return null;
}

export default function GradioWorkbook(props: Props) {
  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <Notifications />
      <Test />
      <AIConfigEditor
        callbacks={props.callbacks}
        aiconfig={props.aiconfig}
        mode="gradio"
      />
    </MantineProvider>
  );
}
