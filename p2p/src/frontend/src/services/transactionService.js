import axios from 'axios';

const API_URL = 'http://localhost:5000/transaction';

export const logTransaction = async (transactionData) => {
    const response = await axios.post(`${API_URL}/log`, transactionData);
    return response.data;
};