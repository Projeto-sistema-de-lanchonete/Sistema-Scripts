-- Banco de dados
create database bdlanchonete;
use bdlanchonete;

-- --------------------------------------------------------
-- Estrutura da tabela `usuarios`

CREATE TABLE `usuarios` (
  `id` int(4) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `senha` varchar(100) NOT NULL
);

-- --------------------------------------------------------
-- chave primaria para tabela `usuarios`

ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

-- --------------------------------------------------------
-- AUTO_INCREMENT de tabela `usuarios`

ALTER TABLE `usuarios`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1000;
COMMIT;

-- --------------------------------------------------------
-- Inserindo dados da tabela `usuarios`

INSERT INTO `usuarios` (nome, cpf, senha) VALUES
('itamar', '08919673462', '1234'),
('eduardathayse', '06576933401', '4321');

select * from usuarios;  -- auto increment

-- deletar linha da tabela  ->>  delete from usuarios where id = 1002;