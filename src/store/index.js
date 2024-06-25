import { createStore } from "vuex";
import axios from "axios";

export default createStore({
  state: {
    carrito: JSON.parse(localStorage.getItem("carrito")) || [],
  },
  mutations: {
    addToCart(state, producto) {
      const item = state.carrito.find(
        (item) => item.ID_HERRAMIENTA === producto.ID_HERRAMIENTA
      );
      if (!item) {
        state.carrito.push({ ...producto, cantidad: 1 });
      } else {
        item.cantidad++;
      }
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
    removeItemsByOne(state, productoId) {
      const item = state.carrito.find(
        (item) => item.ID_HERRAMIENTA === productoId
      );
      if (item && item.cantidad > 1) {
        item.cantidad--;
        localStorage.setItem("carrito", JSON.stringify(state.carrito));
      } else {
        state.carrito = state.carrito.filter(
          (item) => item.ID_HERRAMIENTA !== productoId
        );
      }
    },
    removeTotalFromCart(state, productoId) {
      state.carrito = state.carrito.filter(
        (item) => item.ID_HERRAMIENTA !== productoId
      );
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
    clearCart(state) {
      state.carrito = [];
      localStorage.setItem("carrito", JSON.stringify(state.carrito));
    },
  },
  actions: {
    agregarAlCarrito({ commit }, producto) {
      commit("addToCart", producto);
    },
    borrarItems({ commit }, productoId) {
      commit("removeItemsByOne", productoId);
    },
    removerDelCarrito({ commit }, productoId) {
      commit("removeTotalFromCart", productoId);
    },
    vaciarCarrito({ commit }) {
      commit("clearCart");
    },
    iniciarPago({ getters }){
      const buyOrder = `O-${Date.now()}`;
      const sessionId = `S-${Date.now()}`;
      const amount = parseFloat(getters.totalCarrito.replace(/[^0-9.-]+/g,""));
      const returnUrl = 'http://localhost:5173/store';
      console.log('1');
      return axios.post('http://localhost:5000/api/init_transaction', console.log('2'),{
        buy_order: buyOrder,
        session_id: sessionId,
        amount: amount,
        return_url: returnUrl
      })
      .then(response => {
        console.log('4');
        return response.data.url;
      })
      .catch(error => {
        console.error('Error al iniciar el pago, error: ', error);
        throw error;
      });
    }
  },
  getters: {
    carrito: (state) => state.carrito,
    totalCarrito: (state) => {
      const total = state.carrito.reduce((total, producto) =>{
        return total + producto.VALOR * producto.cantidad;
      }, 0);
      return total.toLocaleString('es-CL', { style: 'currency', currency:'CLP' })
    },
    formatearPrecio: () => (precio) => {
      return precio.toLocaleString('es-CL', { style: 'currency', currency:'CLP' })
    }
  },
});
