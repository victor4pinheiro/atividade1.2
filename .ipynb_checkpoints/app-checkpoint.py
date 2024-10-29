{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fa789c8a-b4ec-4f09-9551-433202df9878",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m\n",
      " * Running on http://127.0.0.1:5001\n",
      "\u001b[33mPress CTRL+C to quit\u001b[0m\n",
      " * Restarting with stat\n",
      "Traceback (most recent call last):\n",
      "  File \"/home/shaka/.local/share/uv/python/cpython-3.10.15-linux-x86_64-gnu/lib/python3.10/runpy.py\", line 196, in _run_module_as_main\n",
      "    return _run_code(code, main_globals, None,\n",
      "  File \"/home/shaka/.local/share/uv/python/cpython-3.10.15-linux-x86_64-gnu/lib/python3.10/runpy.py\", line 86, in _run_code\n",
      "    exec(code, run_globals)\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/ipykernel_launcher.py\", line 18, in <module>\n",
      "    app.launch_new_instance()\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/traitlets/config/application.py\", line 1074, in launch_instance\n",
      "    app.initialize(argv)\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/traitlets/config/application.py\", line 118, in inner\n",
      "    return method(app, *args, **kwargs)\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 692, in initialize\n",
      "    self.init_sockets()\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 331, in init_sockets\n",
      "    self.shell_port = self._bind_socket(self.shell_socket, self.shell_port)\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 253, in _bind_socket\n",
      "    return self._try_bind_socket(s, port)\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/ipykernel/kernelapp.py\", line 229, in _try_bind_socket\n",
      "    s.bind(\"tcp://%s:%i\" % (self.ip, port))\n",
      "  File \"/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/zmq/sugar/socket.py\", line 311, in bind\n",
      "    super().bind(addr)\n",
      "  File \"_zmq.py\", line 917, in zmq.backend.cython._zmq.Socket.bind\n",
      "  File \"_zmq.py\", line 179, in zmq.backend.cython._zmq._check_rc\n",
      "zmq.error.ZMQError: Address already in use (addr='tcp://127.0.0.1:48403')\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/shaka/projects/python/atividade1.2/.venv/lib/python3.10/site-packages/IPython/core/interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Criação da aplicação Flask\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Carregar o modelo treinado (você precisará salvar o modelo como um arquivo .pkl)\n",
    "with open('modelo_regressao.pkl', 'rb') as f:\n",
    "    modelo = pickle.load(f)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predict():\n",
    "    # Obter o valor de horas de estudo do formulário\n",
    "    investimento_marketing = float(request.form['investimento_marketing'])\n",
    "\n",
    "    # Verifica se o atributo existe na requisição\n",
    "    if 'investimento_marketing' not in request.form:\n",
    "        return render_template('erro.html')\n",
    "\n",
    "    # Se estiver vazio, atribua 0 como valor padrão\n",
    "    if not investimento_marketing:\n",
    "        investimento_marketing = 0\n",
    "    \n",
    "    # Transformar a entrada em um array adequado para o modelo\n",
    "    investimento_marketing_array = np.array([[investimento_marketing]])\n",
    "    \n",
    "    # Fazer a previsão usando o modelo\n",
    "    previsao_vendas = modelo.predict(investimento_marketing_array)\n",
    "    \n",
    "    # Retornar o resultado em HTML\n",
    "    return render_template('resultado.html', horas=investimento_marketing, salario=previsao_vendas[0])\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True, port=5000, use_reloader=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fbd6e63-697a-4be7-883f-a6bf24124d36",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.15"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
