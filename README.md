# Aisha Ismail — Portefólio

Site estático com a apresentação pessoal e de serviços, quatro páginas de projeto, demonstração fictícia Atelier Aurora, privacidade e LifeLab geral.

## Conteúdo

- Stellamus: abre o endereço publicado no GitHub Pages, sem copiar a plataforma.
- LifeLab: interface geral recebida em `index(4).html`, com vida guiada ativa na publicação independente. Sem backend de IA. As projeções livres e a preparação automática de pedidos não estão ligadas.
- SENSORA Social: investigação e proposta de cocriação, sem alegar originalidade comprovada, parceria ou eficácia.
- ConduzPT: pacote Godot Chelas Protótipo 02, com requisitos e limitações identificados.

Não existem ligações de navegação para artefactos Claude. Contacto por email, sem envio automático de mensagens ou formulário com backend.

No repositório Portfolio-Aisha, o conteúdo servido está na raiz. O ambiente de construção conserva a cópia em `dist/`. Para atualizar o LifeLab, editar a versão deste repositório e publicar. Alterações noutro serviço não são sincronizadas automaticamente. A Stellamus acompanha as versões publicadas no seu endereço externo.

## Verificações

Sintaxe de todos os scripts; destinos internos e âncoras do portefólio; ausência de URLs Claude; filtros por categoria; navegação por projeto; abertura do LifeLab, perfil e entrada na vida guiada; menu em largura de 390 px e apresentação no computador. A resposta HTTP do endereço Stellamus foi 200. O funcionamento do projeto Godot não foi testado neste ambiente. Não é uma auditoria integral aos conteúdos legais ou financeiros herdados do LifeLab, nem à aplicação externa Stellamus.

## Publicação pública

https://aishaaismaiil.github.io/Portfolio-Aisha/

Os projetos LifeLab, SENSORA e ConduzPT estão organizados neste repositório. O pacote de ConduzPT contém o projeto Godot completo. A Stellamus mantém o seu repositório e publicação independentes.

## Supabase

Sete tabelas com RLS no projeto Supabase Stellamus, com separação lógica por projeto e por utilizador. Migração em `database/schema.sql`, verificação de isolamento em `tests/rls.sql`, configuração pública e adaptador em `backend/`. A migração já foi aplicada, não a executar de novo. O adaptador ainda não está ligado à interface de login/guardar do LifeLab. A IA livre precisa de backend e de um fornecedor configurado no servidor.
