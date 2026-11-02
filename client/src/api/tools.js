import api from "./axios";

export const getTools = async () => {
    const response = await api.get("/tools");
    return response.data['TOOLS'];
}